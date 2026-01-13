"""
Problem 1.4: Green Revolution Impact Analysis
==============================================

This script analyzes the impact of the Green Revolution on wheat yields
in India, performs counterfactual analysis, and estimates population impact.

Author: Dr. Alok Patel
Book: The Pattern Hunters - The Art of Scientific Thinking
Chapter: 1 - The World as a Puzzle
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (15, 12)

# Historical data: Wheat yields in India (kg/hectare)
YEARS = np.array([1960, 1965, 1967, 1970, 1975, 1980, 1985, 1990])
YIELDS = np.array([850, 900, 950, 1450, 1800, 2100, 2300, 2500])

# Context data
INDIA_WHEAT_AREA_1990 = 25  # million hectares
WHEAT_PER_PERSON_YEAR = 70  # kg per person per year
INDIA_POPULATION_1990 = 850  # million people

def identify_inflection_point(years, yields):
    """
    Identify the Green Revolution inflection point using
    change in growth rate.
    
    Parameters:
    -----------
    years : np.array
        Year values
    yields : np.array
        Yield values
    
    Returns:
    --------
    dict : Information about the inflection point
    """
    # Calculate year-over-year growth rates
    growth_rates = np.diff(yields) / np.diff(years)
    
    # Find maximum acceleration (second derivative)
    acceleration = np.diff(growth_rates)
    max_accel_idx = np.argmax(acceleration)
    
    inflection_year_range = (years[max_accel_idx], years[max_accel_idx + 2])
    
    return {
        'range': inflection_year_range,
        'growth_rates': growth_rates,
        'acceleration': acceleration,
        'index': max_accel_idx
    }

def calculate_growth_rates(years, yields, pre_year=1967, post_year=1970):
    """
    Calculate growth rates before and after Green Revolution.
    
    Parameters:
    -----------
    years : np.array
        Year values
    yields : np.array
        Yield values
    pre_year : int
        Cutoff year for pre-GR period
    post_year : int
        Starting year for post-GR period
    
    Returns:
    --------
    dict : Growth rate statistics
    """
    # Pre-Green Revolution
    pre_mask = years <= pre_year
    pre_years = years[pre_mask]
    pre_yields = yields[pre_mask]
    
    pre_slope, pre_intercept, pre_r, pre_p, pre_se = linregress(pre_years, pre_yields)
    
    # Post-Green Revolution
    post_mask = years >= post_year
    post_years = years[post_mask]
    post_yields = yields[post_mask]
    
    post_slope, post_intercept, post_r, post_p, post_se = linregress(post_years, post_yields)
    
    # Calculate percentage growth rates
    pre_total_growth = (pre_yields[-1] - pre_yields[0]) / pre_yields[0] * 100
    pre_annual_rate = pre_total_growth / (pre_years[-1] - pre_years[0])
    
    post_total_growth = (post_yields[-1] - post_yields[0]) / post_yields[0] * 100
    post_annual_rate = post_total_growth / (post_years[-1] - post_years[0])
    
    return {
        'pre': {
            'slope': pre_slope,
            'intercept': pre_intercept,
            'r_squared': pre_r**2,
            'p_value': pre_p,
            'annual_growth': pre_slope,
            'annual_rate': pre_annual_rate,
            'years': pre_years,
            'yields': pre_yields
        },
        'post': {
            'slope': post_slope,
            'intercept': post_intercept,
            'r_squared': post_r**2,
            'p_value': post_p,
            'annual_growth': post_slope,
            'annual_rate': post_annual_rate,
            'years': post_years,
            'yields': post_yields
        }
    }

def counterfactual_analysis(growth_stats, target_year=1990, base_year=1967):
    """
    Calculate what yields would have been without Green Revolution.
    
    Parameters:
    -----------
    growth_stats : dict
        Growth rate statistics
    target_year : int
        Year to project to
    base_year : int
        Base year for projection
    
    Returns:
    --------
    dict : Counterfactual projections
    """
    pre_slope = growth_stats['pre']['slope']
    
    # Linear projection
    base_yield = growth_stats['pre']['yields'][-1]  # 1967 yield
    years_diff = target_year - base_year
    
    linear_projection = base_yield + (pre_slope * years_diff)
    
    # Exponential projection (more realistic)
    annual_rate = growth_stats['pre']['annual_rate'] / 100  # Convert to decimal
    exponential_projection = base_yield * (1 + annual_rate) ** years_diff
    
    # Actual yield in 1990
    actual_1990 = YIELDS[-1]
    
    return {
        'linear': linear_projection,
        'exponential': exponential_projection,
        'actual': actual_1990,
        'difference_linear': actual_1990 - linear_projection,
        'difference_exponential': actual_1990 - exponential_projection,
        'percent_increase_linear': (actual_1990 - linear_projection) / linear_projection * 100,
        'percent_increase_exponential': (actual_1990 - exponential_projection) / exponential_projection * 100
    }

def calculate_population_impact(yield_difference):
    """
    Calculate how many additional people could be fed.
    
    Parameters:
    -----------
    yield_difference : float
        Additional yield per hectare (kg)
    
    Returns:
    --------
    dict : Population impact statistics
    """
    # Total additional production
    additional_production = yield_difference * INDIA_WHEAT_AREA_1990 * 1e6  # kg
    
    # People fed
    people_fed = additional_production / WHEAT_PER_PERSON_YEAR
    
    # Percentage of 1990 population
    percent_population = (people_fed / (INDIA_POPULATION_1990 * 1e6)) * 100
    
    return {
        'additional_production_kg': additional_production,
        'additional_production_tonnes': additional_production / 1000,
        'additional_production_million_tonnes': additional_production / 1e9,
        'people_fed': people_fed,
        'people_fed_millions': people_fed / 1e6,
        'percent_of_population': percent_population
    }

def create_comprehensive_plots(years, yields, growth_stats, counterfactual, inflection):
    """
    Create comprehensive visualization of Green Revolution impact.
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))
    
    # Plot 1: Main timeline with inflection point
    ax1 = axes[0, 0]
    
    # Plot actual data
    ax1.scatter(years, yields, s=150, color='darkgreen', 
                zorder=3, edgecolor='black', linewidth=2, label='Actual Data')
    ax1.plot(years, yields, 'o-', linewidth=2, color='darkgreen', alpha=0.5)
    
    # Highlight inflection period
    ax1.axvspan(inflection['range'][0], inflection['range'][1], 
                alpha=0.3, color='yellow', label='Green Revolution Start')
    
    # Pre-GR trend
    pre_years_extended = np.linspace(1960, 1990, 100)
    pre_trend = growth_stats['pre']['slope'] * pre_years_extended + growth_stats['pre']['intercept']
    ax1.plot(pre_years_extended, pre_trend, '--', color='red', linewidth=2.5,
             label=f'Pre-GR Trend ({growth_stats["pre"]["slope"]:.1f} kg/ha/yr)')
    
    # Post-GR trend
    post_years_extended = np.linspace(1970, 1990, 100)
    post_trend = growth_stats['post']['slope'] * post_years_extended + growth_stats['post']['intercept']
    ax1.plot(post_years_extended, post_trend, '--', color='blue', linewidth=2.5,
             label=f'Post-GR Trend ({growth_stats["post"]["slope"]:.1f} kg/ha/yr)')
    
    # Mark counterfactual 1990
    ax1.scatter([1990], [counterfactual['linear']], s=250, color='red', 
                marker='X', edgecolor='black', linewidth=2.5, zorder=4,
                label='Counterfactual 1990 (without GR)')
    
    # Add annotations
    ax1.annotate('Slow Growth\nPre-Green Revolution', xy=(1962, 875), 
                 fontsize=11, ha='center',
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    ax1.annotate('Rapid Growth\nPost-Green Revolution', xy=(1980, 2350), 
                 fontsize=11, ha='center',
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax1.annotate(f'Gap: {counterfactual["difference_linear"]:.0f} kg/ha\n({counterfactual["percent_increase_linear"]:.1f}% increase)',
                 xy=(1990, (counterfactual['actual'] + counterfactual['linear'])/2),
                 xytext=(1982, 1800), fontsize=11, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', lw=2.5, color='darkgreen'))
    
    ax1.set_xlabel('Year', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Wheat Yield (kg/hectare)', fontsize=13, fontweight='bold')
    ax1.set_title('Green Revolution Impact: Actual vs. Counterfactual', 
                  fontsize=15, fontweight='bold')
    ax1.legend(fontsize=10, loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Growth rates over time
    ax2 = axes[0, 1]
    
    # Calculate growth rates between consecutive years
    annual_growth = np.diff(yields) / np.diff(years)
    growth_years = (years[:-1] + years[1:]) / 2
    
    colors = ['coral' if y < 1970 else 'lightgreen' for y in growth_years]
    bars = ax2.bar(growth_years, annual_growth, width=2, color=colors, 
                   edgecolor='black', alpha=0.8, linewidth=1.5)
    
    # Add average lines
    ax2.axhline(growth_stats['pre']['slope'], color='red', linestyle='--', 
                linewidth=2.5, label=f'Pre-GR Avg: {growth_stats["pre"]["slope"]:.1f} kg/ha/yr')
    ax2.axhline(growth_stats['post']['slope'], color='blue', linestyle='--', 
                linewidth=2.5, label=f'Post-GR Avg: {growth_stats["post"]["slope"]:.1f} kg/ha/yr')
    ax2.axvspan(1967, 1970, alpha=0.2, color='yellow')
    
    ax2.set_xlabel('Year', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Annual Growth Rate (kg/ha/year)', fontsize=13, fontweight='bold')
    ax2.set_title(f'Acceleration in Yield Growth\n' + 
                  f'({growth_stats["post"]["slope"]/growth_stats["pre"]["slope"]:.1f}× faster after GR)',
                  fontsize=15, fontweight='bold')
    ax2.legend(fontsize=11)
    ax2.grid(True, axis='y', alpha=0.3)
    
    # Plot 3: Cumulative gain from Green Revolution
    ax3 = axes[1, 0]
    
    # Counterfactual yields for all years
    counterfactual_all = growth_stats['pre']['slope'] * years + growth_stats['pre']['intercept']
    cumulative_gain = np.maximum(0, yields - counterfactual_all)
    
    # Fill between actual and counterfactual
    ax3.fill_between(years, counterfactual_all, yields,
                     where=(yields > counterfactual_all),
                     color='lightgreen', alpha=0.6, 
                     label='Green Revolution Gain', interpolate=True)
    
    ax3.plot(years, yields, 'o-', linewidth=2.5, markersize=10, 
             color='darkgreen', label='Actual Yield')
    ax3.plot(years, counterfactual_all, 's--', linewidth=2.5, markersize=10,
             color='red', label='Counterfactual (no GR)')
    
    ax3.set_xlabel('Year', fontsize=13, fontweight='bold')
    ax3.set_ylabel('Wheat Yield (kg/hectare)', fontsize=13, fontweight='bold')
    ax3.set_title('Cumulative Yield Gain from Green Revolution', 
                  fontsize=15, fontweight='bold')
    ax3.legend(fontsize=11, loc='upper left')
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Population Impact
    ax4 = axes[1, 1]
    
    # Calculate people fed for each year
    people_fed_timeline = []
    for year, actual_yield in zip(years, yields):
        counterfactual_yield = growth_stats['pre']['slope'] * year + growth_stats['pre']['intercept']
        yield_diff = max(0, actual_yield - counterfactual_yield)
        impact = calculate_population_impact(yield_diff)
        people_fed_timeline.append(impact['people_fed_millions'])
    
    colors_timeline = ['lightcoral' if y < 1970 else 'lightgreen' for y in years]
    bars = ax4.bar(years, people_fed_timeline, width=2, color=colors_timeline,
                   edgecolor='black', alpha=0.8, linewidth=1.5)
    
    ax4.axvspan(1967, 1970, alpha=0.2, color='yellow')
    ax4.set_xlabel('Year', fontsize=13, fontweight='bold')
    ax4.set_ylabel('Additional People Fed (millions)', fontsize=13, fontweight='bold')
    ax4.set_title(f'Green Revolution Food Security Impact\n' +
                  f'({people_fed_timeline[-1]:.0f}M people fed by 1990 = ' +
                  f'{people_fed_timeline[-1]/INDIA_POPULATION_1990*100:.1f}% of population)',
                  fontsize=15, fontweight='bold')
    ax4.grid(True, axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar, value in zip(bars, people_fed_timeline):
        if value > 50:  # Only label significant values
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height,
                    f'{value:.0f}M', ha='center', va='bottom', 
                    fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    return fig

def print_comprehensive_summary(growth_stats, counterfactual, population_impact, inflection):
    """
    Print comprehensive analysis summary.
    """
    print("=" * 90)
    print("GREEN REVOLUTION IMPACT ANALYSIS - INDIA WHEAT YIELDS")
    print("=" * 90)
    
    print("\n📊 1. INFLECTION POINT IDENTIFICATION")
    print("-" * 90)
    print(f"   Green Revolution began: {inflection['range'][0]}-{inflection['range'][1]}")
    print(f"   Visual evidence: Sharp curvature change in yield trajectory")
    print(f"   Historical context: Introduction of high-yielding varieties (HYVs)")
    
    print("\n📈 2. GROWTH RATE ANALYSIS")
    print("-" * 90)
    print(f"   PRE-GREEN REVOLUTION (1960-1967):")
    print(f"      • Annual growth: {growth_stats['pre']['slope']:.2f} kg/ha/year")
    print(f"      • Growth rate: {growth_stats['pre']['annual_rate']:.2f}% per year")
    print(f"      • R² = {growth_stats['pre']['r_squared']:.4f} (fit quality)")
    print(f"      • p-value = {growth_stats['pre']['p_value']:.6f}")
    
    print(f"\n   POST-GREEN REVOLUTION (1970-1990):")
    print(f"      • Annual growth: {growth_stats['post']['slope']:.2f} kg/ha/year")
    print(f"      • Growth rate: {growth_stats['post']['annual_rate']:.2f}% per year")
    print(f"      • R² = {growth_stats['post']['r_squared']:.4f} (fit quality)")
    print(f"      • p-value = {growth_stats['post']['p_value']:.6f}")
    
    print(f"\n   COMPARISON:")
    acceleration = growth_stats['post']['slope'] / growth_stats['pre']['slope']
    print(f"      • Post-GR growth was {acceleration:.1f}× faster!")
    print(f"      • Absolute increase: {growth_stats['post']['slope'] - growth_stats['pre']['slope']:.1f} kg/ha/year")
    
    print("\n🔮 3. COUNTERFACTUAL ANALYSIS (What if no Green Revolution?)")
    print("-" * 90)
    print(f"   Projected 1990 yield (linear model): {counterfactual['linear']:.0f} kg/ha")
    print(f"   Projected 1990 yield (exponential model): {counterfactual['exponential']:.0f} kg/ha")
    print(f"   Actual 1990 yield: {counterfactual['actual']:.0f} kg/ha")
    print(f"\n   IMPACT:")
    print(f"      • Additional yield: {counterfactual['difference_linear']:.0f} kg/ha")
    print(f"      • Percentage improvement: {counterfactual['percent_increase_linear']:.1f}%")
    print(f"      • The Green Revolution nearly DOUBLED yields beyond baseline trend!")
    
    print("\n👥 4. POPULATION IMPACT")
    print("-" * 90)
    print(f"   India's wheat area (1990): {INDIA_WHEAT_AREA_1990} million hectares")
    print(f"   Yield increase per hectare: {counterfactual['difference_linear']:.0f} kg")
    print(f"\n   ADDITIONAL PRODUCTION:")
    print(f"      • Total: {population_impact['additional_production_million_tonnes']:.1f} million tonnes")
    print(f"      • Per year in perpetuity")
    print(f"\n   FOOD SECURITY:")
    print(f"      • People fed: {population_impact['people_fed_millions']:.0f} million")
    print(f"      • Percentage of 1990 population: {population_impact['percent_of_population']:.1f}%")
    print(f"      • This is equivalent to feeding the ENTIRE population of:")
    
    # Country comparisons
    countries = [
        ("Pakistan", 115),
        ("Bangladesh", 110),
        ("Philippines", 60),
        ("United Kingdom", 57),
        ("South Korea", 43)
    ]
    for country, pop in countries:
        if population_impact['people_fed_millions'] > pop:
            print(f"        ✓ {country} (pop: {pop}M)")
    
    print("\n📚 5. HISTORICAL CONTEXT")
    print("-" * 90)
    print("   Key innovations of the Green Revolution:")
    print("      • Semi-dwarf wheat varieties (shorter, stronger stalks)")
    print("      • Disease resistance genes")
    print("      • Fertilizer-responsive varieties")
    print("      • Irrigation expansion")
    print("      • Government support (minimum support prices)")
    print("\n   Impact on India:")
    print("      • 1960s: Food imports, dependent on foreign aid")
    print("      • 1970s: Self-sufficient in wheat production")
    print("      • 2000s: Wheat exporter")
    print("      • Transformation: 'Basket case' → 'Bread basket'")
    
    print("\n⚠️  6. CONFOUNDING VARIABLES TO CONSIDER")
    print("-" * 90)
    print("   This analysis attributes all yield gain to Green Revolution, but:")
    print("      1. Irrigation: Expanded from 25M → 70M hectares")
    print("      2. Fertilizers: Increased 40× (0.3M → 12M tonnes)")
    print("      3. Mechanization: Tractors increased 26× (31K → 800K)")
    print("      4. Policy: Price supports, subsidies, rural credit")
    print("      5. Weather: Some favorable monsoon years")
    print("      6. Extension: Better farmer education and training")
    print("\n   → The 'Green Revolution' was a PACKAGE, not just seeds!")
    print("   → True impact of genetics alone is difficult to isolate")
    
    print("\n💡 7. KEY LESSONS")
    print("-" * 90)
    print("   ✓ Technology alone insufficient - need supporting infrastructure")
    print("   ✓ Policy environment critical for adoption")
    print("   ✓ Multiple inputs work synergistically")
    print("   ✓ Benefits took time to materialize (1967 → 1970s)")
    print("   ✓ Equity concerns: Large farmers benefited more than small")
    print("   ✓ Environmental costs: Water depletion, fertilizer runoff")
    print("   ✓ Sustainability questions remain for future")
    
    print("\n" + "=" * 90)
    print("CONCLUSION: The Green Revolution transformed Indian agriculture and prevented")
    print("widespread famine, enabling population growth and economic development.")
    print("=" * 90 + "\n")

def main():
    """
    Main analysis function.
    """
    print("\n🌾 Starting Green Revolution Impact Analysis...")
    print("=" * 90 + "\n")
    
    # Identify inflection point
    print("Step 1: Identifying Green Revolution inflection point...")
    inflection = identify_inflection_point(YEARS, YIELDS)
    
    # Calculate growth rates
    print("Step 2: Calculating pre- and post-GR growth rates...")
    growth_stats = calculate_growth_rates(YEARS, YIELDS)
    
    # Counterfactual analysis
    print("Step 3: Performing counterfactual analysis...")
    counterfactual = counterfactual_analysis(growth_stats)
    
    # Population impact
    print("Step 4: Calculating population impact...")
    population_impact = calculate_population_impact(counterfactual['difference_linear'])
    
    # Create visualizations
    print("Step 5: Creating comprehensive visualizations...")
    fig = create_comprehensive_plots(YEARS, YIELDS, growth_stats, counterfactual, inflection)
    
    # Save figure
    plt.savefig('green_revolution_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: green_revolution_analysis.png")
    
    # Print summary
    print("\nStep 6: Generating comprehensive report...\n")
    print_comprehensive_summary(growth_stats, counterfactual, population_impact, inflection)
    
    # Show plot
    print("Displaying visualization...")
    plt.show()
    
    print("\n✅ Analysis complete!")
    print("\n📖 This analysis demonstrates:")
    print("   • Pattern recognition in historical data")
    print("   • Inflection point identification")
    print("   • Counterfactual reasoning")
    print("   • Confounding variable awareness")
    print("   • Quantitative impact assessment")

if __name__ == "__main__":
    main()
