"""
Project: Autonomous Thermal Agents in LEO
Architect: Kristine | University of the People
Logic: Predictive 'Survival Instinct' using Agentic Modulation
"""

import random
import time

class RegenerativeThermalAgent:
    def __init__(self):
        # Hardware Constraints
        self.safe_temp_limit = 45.0  # Celsius
        self.critical_temp_limit = 65.0
        
        # System State
        self.internal_temp = 28.5 
        self.coolant_flow_rate = 1.0  # Nominal
        self.shielding_active = False
        self.logs = []

    def get_solar_flux(self):
        """Simulates real-time sensor data from LEO environment."""
        # 1361 W/m2 is the standard; simulating spikes up to 1800 W/m2
        return 1361 + random.randint(-20, 450)

    def predict_and_modulate(self, flux):
        """
        The 'Agent Brick' Logic:
        Predicts thermal load based on flux BEFORE internal temp rises.
        """
        if flux > 1650:
            self.status = "EMERGENCY_REGENERATIVE_SHIELDING"
            self.coolant_flow_rate = 2.5
            self.shielding_active = True
        elif flux > 1450:
            self.status = "PREDICTIVE_FLOW_INCREASE"
            self.coolant_flow_rate = 1.5
            self.shielding_active = False
        else:
            self.status = "NOMINAL_OPERATION"
            self.coolant_flow_rate = 1.0
            self.shielding_active = False

    def update_physics(self, flux):
        """Simulates the thermal exchange within the hardware fabric."""
        # Heat gain is proportional to flux
        heat_gain = (flux / 1361) * 2.2
        # Heat dissipation is boosted by regenerative flow
        heat_loss = self.coolant_flow_rate * 1.8
        
        self.internal_temp += (heat_gain - heat_loss)
        
        # Prevent physical impossibility (cooling below ambient space temp)
        if self.internal_temp < 20.0: self.internal_temp = 20.0

    def run_telemetry(self, cycles=10):
        print(f"{'Cycle':<8} | {'Flux (W/m2)':<12} | {'Temp (C)':<10} | {'Agent Status'}")
        print("-" * 60)
        
        for i in range(cycles):
            flux = self.get_solar_flux()
            self.predict_and_modulate(flux)
            self.update_physics(flux)
            
            # Highlight critical events
            alert = "⚠️" if self.internal_temp > self.safe_temp_limit else " "
            
            print(f"{i+1:<8} | {flux:<12} | {self.internal_temp:<10.2f} | {alert} {self.status}")
            time.sleep(0.1)  # Real-time simulation feel

if __name__ == "__main__":
    agent = RegenerativeThermalAgent()
    agent.run_telemetry()
