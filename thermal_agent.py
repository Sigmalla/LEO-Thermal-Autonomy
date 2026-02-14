"""Module for simulating autonomous thermal management in LEO compute nodes.

This module implements a predictive 'Survival Instinct' logic that modulates
regenerative coolant flow based on external solar flux intensity to prevent 
hardware failure.

Typical usage example:
    agent = RegenerativeThermalAgent()
    agent.run_telemetry(cycles=10)
"""

import random
import time

class RegenerativeThermalAgent:
    """An autonomous agent for regulating orbital hardware temperature.

    Attributes:
        safe_temp_limit: A float representing the maximum operational temperature.
        internal_temp: A float representing the current hardware temperature.
        coolant_flow_rate: A float representing the normalized flow of coolant.
        status: A string representing the current operational mode.
    """

    def __init__(self, start_temp: float = 28.5):
        """Initializes the agent with default hardware constraints."""
        self.safe_temp_limit = 45.0
        self.internal_temp = start_temp
        self.coolant_flow_rate = 1.0
        self.status = "NOMINAL_OPERATION"

    def get_solar_flux(self) -> float:
        """Simulates sensor input for external solar flux in W/m^2.

        Returns:
            A float representing the current solar flux intensity.
        """
        # Baseline solar constant is ~1361 W/m2
        return 1361 + random.randint(-20, 450)

    def predict_and_modulate(self, flux: float):
        """Predicts thermal load and modulates coolant flow proactively.

        Args:
            flux: The current solar flux intensity measured in Watts/m^2.
        """
        if flux > 1650:
            self.status = "EMERGENCY_REGENERATIVE_SHIELDING"
            self.coolant_flow_rate = 2.5
        elif flux > 1450:
            self.status = "PREDICTIVE_FLOW_INCREASE"
            self.coolant_flow_rate = 1.5
        else:
            self.status = "NOMINAL_OPERATION"
            self.coolant_flow_rate = 1.0

    def update_physics(self, flux: float):
        """Calculates internal temperature based on flux and dissipation.

        Args:
            flux: The current external solar flux intensity.
        """
        heat_gain = (flux / 1361) * 2.2
        heat_dissipation = self.coolant_flow_rate * 1.8
        
        self.internal_temp += (heat_gain - heat_dissipation)
        
        # Ensure temperature stays within physical LEO boundaries
        if self.internal_temp < 20.0:
            self.internal_temp = 20.0

    def run_telemetry(self, cycles: int = 10):
        """Executes a simulation loop and prints system telemetry.

        Args:
            cycles: The number of simulation steps to execute.
        """
        print(f"{'Cycle':<8} | {'Flux (W/m2)':<12} | {'Temp (C)':<10} | Status")
        print("-" * 65)
        
        for i in range(cycles):
            flux = self.get_solar_flux()
            self.predict_and_modulate(flux)
            self.update_physics(flux)
            
            # Identify critical thermal events
            alert = "!" if self.internal_temp > self.safe_temp_limit else " "
            
            print(f"{i+1:<8} | {flux:<12} | {self.internal_temp:<10.2f} | {alert}{self.status}")
            time.sleep(0.1)

if __name__ == "__main__":
    # Create the agent and launch the orbital simulation
    orbital_agent = RegenerativeThermalAgent()
    orbital_agent.run_telemetry(cycles=15)
