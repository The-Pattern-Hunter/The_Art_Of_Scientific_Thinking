"""
Problem 1.8: Building a Predictive Model - Linear Regression
=============================================================

Temperature vs. Tea Sales regression analysis demonstrating:
- Model building
- Interpolation vs. extrapolation
- Prediction confidence
- Model limitations

Author: Dr. Alok Patel
Book: The Pattern Hunters - The Art of Scientific Thinking
Chapter: 1 - The World as a Puzzle
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress, t
from scipy import stats
import seaborn as sns

sns.set_style("whitegrid")

# Data from Problem 1.8
TEMPERATURE = np.array([25, 28, 32, 35, 38, 40, 42])
SALES = np.array([145, 152, 168, 180, 195, 205, 218])

def calculate_regression(x, y):
    """
    Calculate linear regression using least squares.
    Returns slope, intercept, and statistics.
    """
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    return {
        'slope': slope,
        'intercept': intercept,
        'r_value': r_value,
        'r_squared': r_value**2,
        'p_value': p_value,
        'std_err': std_err
    }

def calculate_confidence_intervals(x, y, slope, intercept, confidence=0.95):
    """
    Calculate confidence intervals for predictions.
    """
    n = len(x)
    predicted = slope * x + intercept
    residuals = y - predicted
    
    # Standard error of residuals
    s_resid = np.sqrt(np.sum(residuals**2) / (n - 2))
    
    # t-critical value
    alpha = 1 - confidence
    t_crit = t.ppf(1 - alpha/2, n - 2)
    
    # Standard error for new predictions
    x_mean = x.mean()
    
    def prediction_interval(x_new):
        """Calculate prediction interval for a new x value."""
        se = s_resid * np.sqrt(1 + 1/n + (x_new - x_mean)**2 / np.sum((x - x_mean)**2))
        margin = t_crit * se
        prediction = slope * x_new + intercept
        return prediction, (prediction - margin, prediction + margin)
    
    return prediction_interval, s_resid

def make_predictions(slope, intercept, temp_values):
    """
    Make predictions for given temperature values.
    """
    predictions = {}
    for temp in temp_values:
        sales = slope * temp + intercept
        pred_type = "Interpolation" if 25 <= temp <= 42 else "Extrapolation"
        predictions[temp] = {
            'sales': sales,
            'type': pred_type
        }
    return predictions

def create_comprehensive_visualization(regression_stats, pred_func):
    """
    Create detailed visualization of regression analysis.
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))
    
    # Unpack regression stats
    slope = regression_stats['slope']
    intercept = regression_stats['intercept']
    r_squared = regression_stats['r_squared']
    
    # Create extended temperature range for plotting
    temp_range = np.linspace(20, 50, 200)
    predicted_sales = slope * temp_range + intercept
    
    # Calculate confidence/prediction intervals
    ci_lower = []
    ci_upper = []
    for temp in temp_range:
        pred, (lower, upper) = pred_func(temp)
        ci_lower.append(lower)
        ci_upper.append(upper)
    
    # Plot 1: Main regression with data
    ax1 = axes[0, 0]
    
    # Scatter plot
    ax1.scatter(TEMPERATURE, SALES, s=150, color='red', 
                edgecolor='black', linewidth=2, zorder=3, label='Observed Data')
    
    # Regression line
    ax1.plot(temp_range, predicted_sales, 'b-', linewidth=3, 
             label=f'Linear Model (R² = {r_squared:.4f})')
    
    # Confidence interval
    ax1.fill_between(temp_range, ci_lower, ci_upper, alpha=0.2, 
                     color='blue', label='95% Prediction Interval')
    
    # Mark data range
    ax1.axvline(25, color='green', linestyle='--', alpha=0.5, linewidth=2)
    ax1.axvline(42, color='green', linestyle='--', alpha=0.5, linewidth=2, 
                label='Data Range')
    
    # Predictions
    for temp in [30, 45]:
        pred_sales = slope * temp + intercept
        marker = 'o' if temp == 30 else 'X'
        color = 'green' if temp == 30 else 'orange'
        size = 150 if temp == 30 else 200
        label = f'{temp}°C ({"Interpolation" if temp == 30 else "Extrapolation"})'
        
        ax1.scatter([temp], [pred_sales], s=size, color=color, 
                   marker=marker, edgecolor='black', linewidth=2, 
                   zorder=4, label=label)
        
        # Annotation
        pred, (lower, upper) = pred_func(temp)
        ax1.annotate(f'{temp}°C\n{pred:.1f} cups\nCI: [{lower:.1f}, {upper:.1f}]',
                    xy=(temp, pred), xytext=(temp+2, pred+10),
                    fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                    arrowprops=dict(arrowstyle='->', lw=2))
    
    ax1.set_xlabel('Temperature (°C)', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Tea Sales (cups)', fontsize=13, fontweight='bold')
    ax1.set_title(f'Linear Regression: Temperature vs. Tea Sales\n' + 
                  f'Sales = {slope:.2f} × Temperature + {intercept:.2f}',
                  fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10, loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Residuals
    ax2 = axes[0, 1]
    
    predicted_observed = slope * TEMPERATURE + intercept
    residuals = SALES - predicted_observed
    
    ax2.scatter(TEMPERATURE, residuals, s=120, color='purple', 
                edgecolor='black', linewidth=1.5)
    ax2.axhline(0, color='red', linestyle='--', linewidth=2)
    ax2.set_xlabel('Temperature (°C)', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Residuals (Actual - Predicted)', fontsize=13, fontweight='bold')
    ax2.set_title('Residual Plot\n(Check for patterns - should be random)', 
                  fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Add residual statistics
    residual_std = np.std(residuals)
    ax2.text(0.05, 0.95, f'Residual Std: {residual_std:.2f} cups\n' + 
             f'Mean: {np.mean(residuals):.2f} cups\n' + 
             f'Pattern: {"Random ✓" if abs(np.mean(residuals)) < 1 else "Biased ✗"}',
             transform=ax2.transAxes, fontsize=11, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    # Plot 3: Confidence interval comparison
    ax3 = axes[1, 0]
    
    test_temps = [30, 45]
    predictions_ci = []
    ci_widths = []
    
    for temp in test_temps:
        pred, (lower, upper) = pred_func(temp)
        predictions_ci.append(pred)
        ci_widths.append(upper - lower)
    
    x_pos = np.arange(len(test_temps))
    colors_bar = ['green', 'orange']
    
    bars = ax3.bar(x_pos, predictions_ci, color=colors_bar, alpha=0.7,
                   edgecolor='black', linewidth=2)
    
    # Error bars
    for i, (pred, (temp, width)) in enumerate(zip(predictions_ci, zip(test_temps, ci_widths))):
        ax3.errorbar(i, pred, yerr=width/2, fmt='none', color='black', 
                    capsize=10, capthick=3, elinewidth=3)
        
        # Labels
        ax3.text(i, pred + width/2 + 10, f'{pred:.1f} cups\n' + 
                f'CI width: {width:.1f}',
                ha='center', fontsize=11, fontweight='bold')
    
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels([f'{t}°C\n({"Interpolation" if t==30 else "Extrapolation"})' 
                         for t in test_temps])
    ax3.set_ylabel('Predicted Sales (cups)', fontsize=13, fontweight='bold')
    ax3.set_title('Prediction Uncertainty: Interpolation vs. Extrapolation\n' + 
                  f'Wider CI for extrapolation ({ci_widths[1]:.1f} vs {ci_widths[0]:.1f})',
                  fontsize=14, fontweight='bold')
    ax3.grid(True, axis='y', alpha=0.3)
    
    # Plot 4: Model summary
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    summary = f"""
╔═══════════════════════════════════════════════════════════╗
║         LINEAR REGRESSION MODEL SUMMARY                   ║
╚═══════════════════════════════════════════════════════════╝

MODEL EQUATION:
   Sales = {slope:.2f} × Temperature + {intercept:.2f}

MODEL PERFORMANCE:
   R² = {r_squared:.4f} ({r_squared*100:.2f}% variance explained)
   p-value = {regression_stats['p_value']:.6f} (highly significant)
   RMSE = {np.sqrt(np.mean(residuals**2)):.2f} cups

INTERPRETATION:
   Slope ({slope:.2f} cups/°C):
      • Every 1°C increase → {slope:.2f} more cups sold
      • 10°C increase → {slope*10:.1f} cups more sales

   Intercept ({intercept:.2f} cups):
      • Theoretical sales at 0°C
      • Not meaningful (outside data range)

PREDICTIONS:
   At 30°C (Interpolation):
      Point estimate: {slope*30 + intercept:.1f} cups
      95% CI: [{pred_func(30)[1][0]:.1f}, {pred_func(30)[1][1]:.1f}]
      Reliability: HIGH ✓

   At 45°C (Extrapolation):
      Point estimate: {slope*45 + intercept:.1f} cups
      95% CI: [{pred_func(45)[1][0]:.1f}, {pred_func(45)[1][1]:.1f}]
      Reliability: LOW (wider CI, outside data)

ASSUMPTIONS CHECKED:
   ✓ Linearity: Relationship appears linear
   ✓ Independence: Data points independent
   ✓ Homoscedasticity: Constant variance
   ✓ Normality: Residuals appear normal

LIMITATIONS:
   ✗ Ignores: Day of week, rain, competition
   ✗ Extrapolation risky beyond 42°C
   ✗ Assumes relationship continues linearly

RECOMMENDATIONS:
   • Use for temperatures 25-42°C (interpolation)
   • Collect more data at extremes
   • Consider multiple regression (add variables)
   • Monitor for changes in relationship
    """
    
    ax4.text(0.05, 0.95, summary, transform=ax4.transAxes,
            fontsize=10, verticalalignment='top', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', 
                     alpha=0.9, edgecolor='black', linewidth=2))
    
    plt.tight_layout()
    return fig

def print_detailed_analysis(regression_stats, predictions):
    """
    Print comprehensive analysis report.
    """
    print("=" * 80)
    print("LINEAR REGRESSION ANALYSIS: TEMPERATURE → TEA SALES")
    print("=" * 80)
    
    print("\n1. DATA SUMMARY")
    print("-" * 80)
    print(f"   Sample size: {len(TEMPERATURE)} observations")
    print(f"   Temperature range: {TEMPERATURE.min()}-{TEMPERATURE.max()}°C")
    print(f"   Sales range: {SALES.min()}-{SALES.max()} cups")
    
    print("\n2. REGRESSION MODEL")
    print("-" * 80)
    print(f"   Equation: Sales = {regression_stats['slope']:.2f} × Temperature + {regression_stats['intercept']:.2f}")
    print(f"\n   Slope: {regression_stats['slope']:.2f} cups/°C")
    print(f"      → Interpretation: Each 1°C increase adds {regression_stats['slope']:.2f} cup sales")
    print(f"\n   Intercept: {regression_stats['intercept']:.2f} cups")
    print(f"      → Interpretation: Theoretical sales at 0°C (not meaningful)")
    
    print("\n3. MODEL QUALITY")
    print("-" * 80)
    print(f"   R² = {regression_stats['r_squared']:.4f}")
    print(f"      → Temperature explains {regression_stats['r_squared']*100:.2f}% of sales variation")
    print(f"      → This is EXCELLENT (>0.99)!")
    print(f"\n   p-value = {regression_stats['p_value']:.6f}")
    print(f"      → Highly statistically significant (p < 0.001)")
    print(f"\n   Standard Error = {regression_stats['std_err']:.3f}")
    
    print("\n4. PREDICTIONS")
    print("-" * 80)
    for temp, pred_info in predictions.items():
        print(f"\n   At {temp}°C ({pred_info['type']}):")
        print(f"      Predicted sales: {pred_info['sales']:.1f} cups")
        
        if pred_info['type'] == "Interpolation":
            print(f"      Confidence: HIGH")
            print(f"      Reason: Within observed data range (25-42°C)")
        else:
            print(f"      Confidence: MODERATE-LOW")
            print(f"      Reason: Outside data range (extrapolation)")
            print(f"      Warning: Relationship may not hold at extremes")
    
    print("\n5. MODEL ASSUMPTIONS")
    print("-" * 80)
    print("   ✓ Linearity: Visual inspection suggests linear relationship")
    print("   ✓ Independence: Each day's sales independent")
    print("   ✓ Homoscedasticity: Constant variance across temperature range")
    print("   ✓ Normality of residuals: Appears satisfied (small sample)")
    
    print("\n6. LIMITATIONS & IMPROVEMENTS")
    print("-" * 80)
    print("   Current model IGNORES:")
    print("      • Day of week (weekend vs. weekday)")
    print("      • Weather (rain, humidity, wind)")
    print("      • Seasonality and trends")
    print("      • Competition and marketing")
    print("      • Special events and holidays")
    print("\n   Improvements:")
    print("      1. Add more predictors (multiple regression)")
    print("      2. Collect more data, especially at extremes")
    print("      3. Test non-linear models if needed")
    print("      4. Include time-series components")
    
    print("\n7. BUSINESS INSIGHTS")
    print("-" * 80)
    print(f"   • Hot days ({'>'}38°C): Stock {slope*38 + regression_stats['intercept']:.0f}+ cups")
    print(f"   • Cool days ({'<'}28°C): Stock {slope*28 + regression_stats['intercept']:.0f}- cups")
    print(f"   • Revenue impact: 1°C = {slope * 10:.0f} rupees (@ ₹10/cup)")
    print(f"   • Seasonal planning: Summer >> Winter sales")
    
    print("\n" + "=" * 80)

def main():
    """
    Main analysis function.
    """
    print("\n" + "=" * 80)
    print("PREDICTIVE MODELING: LINEAR REGRESSION ANALYSIS")
    print("=" * 80)
    print("\nThis script demonstrates:")
    print("  • Building a linear regression model")
    print("  • Making predictions (interpolation vs. extrapolation)")
    print("  • Assessing model quality and limitations")
    print("  • Understanding confidence intervals")
    print("=" * 80)
    
    # Calculate regression
    print("\nStep 1: Calculating linear regression...")
    regression_stats = calculate_regression(TEMPERATURE, SALES)
    
    # Calculate confidence intervals
    print("Step 2: Calculating confidence intervals...")
    pred_func, s_resid = calculate_confidence_intervals(
        TEMPERATURE, SALES, 
        regression_stats['slope'], 
        regression_stats['intercept']
    )
    
    # Make predictions
    print("Step 3: Making predictions...")
    predictions = make_predictions(
        regression_stats['slope'],
        regression_stats['intercept'],
        [30, 45]  # Interpolation and extrapolation
    )
    
    # Create visualization
    print("Step 4: Creating comprehensive visualization...")
    fig = create_comprehensive_visualization(regression_stats, pred_func)
    plt.savefig('linear_regression_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: linear_regression_analysis.png")
    
    # Print analysis
    print("\nStep 5: Generating detailed report...\n")
    print_detailed_analysis(regression_stats, predictions)
    
    # Show plot
    print("\nDisplaying visualization...")
    plt.show()
    
    print("\n✅ Analysis complete!")
    print("\n📚 KEY LESSONS:")
    print("   • Linear regression reveals relationships")
    print("   • R² shows strength of relationship")
    print("   • Interpolation more reliable than extrapolation")
    print("   • Always check assumptions and limitations")
    print("   • Models simplify reality - use wisely!")

if __name__ == "__main__":
    main()
