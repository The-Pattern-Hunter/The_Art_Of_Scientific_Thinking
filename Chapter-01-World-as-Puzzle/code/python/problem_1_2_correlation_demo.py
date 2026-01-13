"""
Problem 1.2: Correlation vs. Causation Demonstration
=====================================================

This script demonstrates the classic "ice cream vs. drowning" example
of spurious correlation caused by a confounding variable (temperature).

Author: Dr. Alok Patel
Book: The Pattern Hunters - The Art of Scientific Thinking
Chapter: 1 - The World as a Puzzle
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)

def generate_data(n_months=12, seed=42):
    """
    Generate simulated data for ice cream sales, drowning deaths,
    and the confounding variable (temperature).
    
    Parameters:
    -----------
    n_months : int
        Number of months to simulate (default: 12 for one year)
    seed : int
        Random seed for reproducibility
    
    Returns:
    --------
    dict : Dictionary containing temperature, ice_cream, and drowning data
    """
    np.random.seed(seed)
    
    # Months (1-12)
    months = np.arange(1, n_months + 1)
    
    # Temperature follows seasonal pattern (sine wave)
    # Peaks in summer (month 7), lowest in winter (month 1, 12)
    temperature = 15 + 15 * np.sin((months - 3) * np.pi / 6) + np.random.normal(0, 2, n_months)
    
    # Ice cream sales caused by temperature + noise
    ice_cream = 50 + 10 * temperature + np.random.normal(0, 20, n_months)
    
    # Swimming activity also caused by temperature
    swimming_activity = 10 + 2 * temperature + np.random.normal(0, 5, n_months)
    
    # Drowning deaths caused by swimming activity (not ice cream!)
    drowning = 2 + 0.3 * swimming_activity + np.random.normal(0, 1, n_months)
    
    return {
        'months': months,
        'temperature': temperature,
        'ice_cream': ice_cream,
        'drowning': drowning,
        'swimming': swimming_activity
    }

def calculate_correlations(data):
    """
    Calculate all relevant correlation coefficients.
    
    Parameters:
    -----------
    data : dict
        Dictionary containing the data arrays
    
    Returns:
    --------
    dict : Dictionary of correlation coefficients
    """
    correlations = {
        'ice_cream_drowning': stats.pearsonr(data['ice_cream'], data['drowning']),
        'temp_ice_cream': stats.pearsonr(data['temperature'], data['ice_cream']),
        'temp_drowning': stats.pearsonr(data['temperature'], data['drowning']),
        'temp_swimming': stats.pearsonr(data['temperature'], data['swimming']),
        'swimming_drowning': stats.pearsonr(data['swimming'], data['drowning'])
    }
    return correlations

def calculate_partial_correlation(data):
    """
    Calculate partial correlation between ice cream and drowning,
    controlling for temperature (the confounding variable).
    
    Parameters:
    -----------
    data : dict
        Dictionary containing the data arrays
    
    Returns:
    --------
    float : Partial correlation coefficient
    """
    # Remove temperature effect from ice cream
    ice_cream_resid = data['ice_cream'] - np.polyval(
        np.polyfit(data['temperature'], data['ice_cream'], 1), 
        data['temperature']
    )
    
    # Remove temperature effect from drowning
    drowning_resid = data['drowning'] - np.polyval(
        np.polyfit(data['temperature'], data['drowning'], 1), 
        data['temperature']
    )
    
    # Correlation of residuals = partial correlation
    partial_corr = stats.pearsonr(ice_cream_resid, drowning_resid)
    
    return partial_corr, ice_cream_resid, drowning_resid

def create_visualizations(data, correlations, partial_data):
    """
    Create comprehensive visualizations showing spurious correlation.
    
    Parameters:
    -----------
    data : dict
        Dictionary containing the data arrays
    correlations : dict
        Dictionary of correlation coefficients
    partial_data : tuple
        Partial correlation result and residuals
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Unpack partial correlation data
    partial_corr, ice_cream_resid, drowning_resid = partial_data
    
    # Color mapping by temperature
    colors = data['temperature']
    
    # Plot 1: The Misleading Correlation (Ice Cream vs Drowning)
    ax1 = axes[0, 0]
    scatter1 = ax1.scatter(data['ice_cream'], data['drowning'], 
                           c=colors, cmap='YlOrRd', s=120, 
                           edgecolor='black', linewidth=1.5, alpha=0.8)
    
    # Add regression line
    z = np.polyfit(data['ice_cream'], data['drowning'], 1)
    p = np.poly1d(z)
    ice_cream_range = np.linspace(data['ice_cream'].min(), data['ice_cream'].max(), 100)
    ax1.plot(ice_cream_range, p(ice_cream_range), "r--", 
             alpha=0.8, linewidth=3, label='Misleading trend line')
    
    ax1.set_xlabel('Ice Cream Sales', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Drowning Deaths', fontsize=13, fontweight='bold')
    ax1.set_title(f'❌ MISLEADING Correlation (r = {correlations["ice_cream_drowning"][0]:.3f})\n' +
                  f'"Ice cream causes drowning?" NO!', 
                  fontsize=14, fontweight='bold', color='red')
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)
    
    # Add colorbar
    cbar1 = plt.colorbar(scatter1, ax=ax1)
    cbar1.set_label('Temperature (°C)', fontsize=11)
    
    # Plot 2: The True Cause - Temperature vs Ice Cream
    ax2 = axes[0, 1]
    ax2.scatter(data['temperature'], data['ice_cream'], 
                c='dodgerblue', s=120, alpha=0.7, 
                edgecolor='black', linewidth=1.5)
    
    # Add regression line
    z = np.polyfit(data['temperature'], data['ice_cream'], 1)
    p = np.poly1d(z)
    temp_range = np.linspace(data['temperature'].min(), data['temperature'].max(), 100)
    ax2.plot(temp_range, p(temp_range), "b--", alpha=0.8, linewidth=3)
    
    ax2.set_xlabel('Temperature (°C)', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Ice Cream Sales', fontsize=13, fontweight='bold')
    ax2.set_title(f'✓ TRUE Causation: Temperature → Ice Cream\n' +
                  f'(r = {correlations["temp_ice_cream"][0]:.3f})', 
                  fontsize=14, fontweight='bold', color='green')
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: The True Cause - Temperature → Swimming → Drowning
    ax3 = axes[1, 0]
    ax3.scatter(data['temperature'], data['drowning'], 
                c='crimson', s=120, alpha=0.7, 
                edgecolor='black', linewidth=1.5)
    
    # Add regression line
    z = np.polyfit(data['temperature'], data['drowning'], 1)
    p = np.poly1d(z)
    ax3.plot(temp_range, p(temp_range), "r--", alpha=0.8, linewidth=3)
    
    ax3.set_xlabel('Temperature (°C)', fontsize=13, fontweight='bold')
    ax3.set_ylabel('Drowning Deaths', fontsize=13, fontweight='bold')
    ax3.set_title(f'✓ TRUE Causation: Temperature → Swimming → Drowning\n' +
                  f'(r = {correlations["temp_drowning"][0]:.3f})', 
                  fontsize=14, fontweight='bold', color='green')
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Partial Correlation (Controlling for Temperature)
    ax4 = axes[1, 1]
    ax4.scatter(ice_cream_resid, drowning_resid, 
                c='purple', s=120, alpha=0.7, 
                edgecolor='black', linewidth=1.5)
    
    # Add reference lines
    ax4.axhline(y=0, color='gray', linestyle='--', alpha=0.5, linewidth=2)
    ax4.axvline(x=0, color='gray', linestyle='--', alpha=0.5, linewidth=2)
    
    # Add regression line (should be nearly flat!)
    z = np.polyfit(ice_cream_resid, drowning_resid, 1)
    p = np.poly1d(z)
    resid_range = np.linspace(ice_cream_resid.min(), ice_cream_resid.max(), 100)
    ax4.plot(resid_range, p(resid_range), "k--", alpha=0.8, linewidth=3, 
             label=f'Slope ≈ {z[0]:.4f} (nearly zero!)')
    
    ax4.set_xlabel('Ice Cream Sales\n(temperature effect removed)', 
                   fontsize=13, fontweight='bold')
    ax4.set_ylabel('Drowning Deaths\n(temperature effect removed)', 
                   fontsize=13, fontweight='bold')
    ax4.set_title(f'✓ Partial Correlation (r = {partial_corr[0]:.3f})\n' +
                  f'"No relationship after controlling for temperature!"', 
                  fontsize=14, fontweight='bold', color='green')
    ax4.legend(fontsize=11)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

def create_causal_diagram():
    """
    Create a simple causal diagram showing the relationships.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    
    # Title
    ax.text(0.5, 0.95, 'Causal Structure: The Confounding Variable', 
            ha='center', fontsize=18, fontweight='bold', 
            transform=ax.transAxes)
    
    # Draw the diagram
    diagram_text = """
    
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │                    TEMPERATURE                          │
    │                   (Confounding                          │
    │                    Variable)                            │
    │                         │                               │
    │           ┌─────────────┴─────────────┐                 │
    │           │                           │                 │
    │           ↓                           ↓                 │
    │     ICE CREAM                    SWIMMING               │
    │       SALES                      ACTIVITY               │
    │           │                           │                 │
    │           │                           ↓                 │
    │           │                      DROWNING               │
    │           │                       DEATHS                │
    │           │                           ↑                 │
    │           └───────────────────────────┘                 │
    │              (Spurious correlation,                     │
    │               NOT causation!)                           │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
    
    KEY INSIGHT:
    ============
    • Temperature CAUSES both ice cream sales and swimming
    • Swimming CAUSES drowning (more swimmers = more risk)
    • Ice cream and drowning are CORRELATED
    • But ice cream does NOT CAUSE drowning!
    • They share a COMMON CAUSE (temperature)
    
    STATISTICAL EVIDENCE:
    ====================
    • Direct correlation: r ≈ 0.87 (looks like causation!)
    • Partial correlation: r ≈ 0.12 (NO relationship!)
    • After controlling for temperature, correlation disappears
    
    LESSON:
    =======
    "Correlation does not imply causation!"
    Always look for confounding variables!
    """
    
    ax.text(0.05, 0.85, diagram_text, 
            ha='left', va='top', fontsize=11, 
            family='monospace',
            transform=ax.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', 
                     alpha=0.8, edgecolor='black', linewidth=2))
    
    return fig

def print_summary(correlations, partial_corr):
    """
    Print a comprehensive summary of the analysis.
    
    Parameters:
    -----------
    correlations : dict
        Dictionary of correlation coefficients
    partial_corr : tuple
        Partial correlation result
    """
    print("=" * 80)
    print("SPURIOUS CORRELATION DEMONSTRATION")
    print("Ice Cream Sales vs. Drowning Deaths")
    print("=" * 80)
    
    print("\n1. MISLEADING DIRECT CORRELATION:")
    print(f"   Ice Cream vs Drowning: r = {correlations['ice_cream_drowning'][0]:.3f}")
    print(f"   p-value: {correlations['ice_cream_drowning'][1]:.6f}")
    print("   → Suggests strong relationship! (WRONG)")
    
    print("\n2. TRUE CAUSAL RELATIONSHIPS:")
    print(f"   Temperature vs Ice Cream: r = {correlations['temp_ice_cream'][0]:.3f}")
    print(f"   Temperature vs Drowning: r = {correlations['temp_drowning'][0]:.3f}")
    print(f"   Temperature vs Swimming: r = {correlations['temp_swimming'][0]:.3f}")
    print(f"   Swimming vs Drowning: r = {correlations['swimming_drowning'][0]:.3f}")
    print("   → Temperature causes BOTH variables")
    
    print("\n3. PARTIAL CORRELATION (controlling for temperature):")
    print(f"   Ice Cream vs Drowning (controlled): r = {partial_corr[0]:.3f}")
    print(f"   p-value: {partial_corr[1]:.6f}")
    print("   → No relationship after controlling for confound!")
    
    print("\n4. INTERPRETATION:")
    if abs(correlations['ice_cream_drowning'][0]) > 0.7:
        print("   ✗ Direct correlation is STRONG (misleading!)")
    if abs(partial_corr[0]) < 0.3:
        print("   ✓ Partial correlation is WEAK (truth revealed!)")
    
    print("\n5. CONCLUSION:")
    print("   Temperature is a CONFOUNDING VARIABLE that causes both:")
    print("   • Ice cream sales (people buy ice cream when hot)")
    print("   • Drowning deaths (people swim more when hot → more accidents)")
    print("\n   Ice cream and drowning are correlated but NOT causally related!")
    print("\n" + "=" * 80)
    
    print("\n📚 LESSON: Always ask three questions:")
    print("   1. Is there correlation? (statistics)")
    print("   2. Is there a mechanism? (biology/physics)")
    print("   3. Is there experimental evidence? (causation)")
    print("\n   Only when ALL THREE align can we claim causation!")
    print("=" * 80)

def main():
    """
    Main function to run the complete demonstration.
    """
    print("\nGenerating simulated data...")
    data = generate_data(n_months=12, seed=42)
    
    print("Calculating correlations...")
    correlations = calculate_correlations(data)
    
    print("Calculating partial correlation (controlling for temperature)...")
    partial_data = calculate_partial_correlation(data)
    
    print("\nCreating visualizations...")
    fig1 = create_visualizations(data, correlations, partial_data)
    plt.savefig('correlation_vs_causation_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: correlation_vs_causation_analysis.png")
    
    fig2 = create_causal_diagram()
    plt.savefig('causal_diagram.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: causal_diagram.png")
    
    print("\nDisplaying summary...")
    print_summary(correlations, partial_data[0])
    
    print("\nShowing plots...")
    plt.show()
    
    print("\n✅ Analysis complete!")
    print("\nKEY TAKEAWAY:")
    print("This demonstrates why 'correlation ≠ causation' is so important")
    print("in scientific thinking. Always look for confounding variables!")

if __name__ == "__main__":
    main()
