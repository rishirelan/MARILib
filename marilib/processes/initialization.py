#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 23:22:21 2019

@author: DRUOT Thierry : original Scilab implementation
         PETEILH Nicolas : portage to Python
"""

import numpy

from marilib.tools import units as unit


#===========================================================================================================
def ref_cruise_altp(propulsive_architecture):
    if (propulsive_architecture==1):
        ref_cruise_altp_i = unit.m_ft(35000)
    elif (propulsive_architecture==2):
        ref_cruise_altp_i = unit.m_ft(35000)
    else:
        raise Exception("propulsion.architecture index is out of range")
    return ref_cruise_altp_i

#===========================================================================================================
def top_of_climb_altp(propulsive_architecture):
    if (propulsive_architecture==1):
        top_of_climb_altp_i = unit.m_ft(31000)
    elif (propulsive_architecture==2):
        top_of_climb_altp_i = unit.m_ft(31000)
    else:
        raise Exception("propulsion.architecture index is out of range")
    return top_of_climb_altp_i


#===========================================================================================================
def n_pax_front(n_pax_ref):
    if  (n_pax_ref<=8):   n_pax_front_i = 2
    elif(n_pax_ref<=16):  n_pax_front_i = 3
    elif(n_pax_ref<=50):  n_pax_front_i = 4
    elif(n_pax_ref<=120): n_pax_front_i = 5
    elif(n_pax_ref<=225): n_pax_front_i = 6
    elif(n_pax_ref<=300): n_pax_front_i = 8
    elif(n_pax_ref<=375): n_pax_front_i = 9
    else:                 n_pax_front_i = 10
    return n_pax_front_i

#===========================================================================================================
def n_aisle(n_pax_front):
    if(n_pax_front <= 6): n_aisle_i = 1
    else:                 n_aisle_i = 2
    return n_aisle_i

#===========================================================================================================
def m_pax_nominal(design_range):
    if(design_range <= unit.m_NM(3500)):
        m_pax_nominal_i = 100
    elif(design_range <= unit.m_NM(5500)):
        m_pax_nominal_i = 105
    else:
        m_pax_nominal_i = 110
    return m_pax_nominal_i

#===========================================================================================================
def m_pax_max(design_range):
    if(design_range <= unit.m_NM(3500)):
        m_pax_max_i = 120
    elif(design_range <= unit.m_NM(5500)):
        m_pax_max_i = 135
    else:
        m_pax_max_i = 150
    return m_pax_max_i

#===========================================================================================================
def cg_range_optimization():
    cg_range_optimization_i = 0       # Wing position, HTP area and VTP area optimized according to HQ criteria, 0: no, 1:yes
    return cg_range_optimization_i

#===========================================================================================================
def wing_attachment():
    """
    wing_attachment = 1 : low wing
    wing_attachment = 2 : high wing
    """
    wing_attachment_i = 1
    return wing_attachment_i

#===========================================================================================================
def wing_morphing():
    """
    wing_morphing = 1 : aspect ratio is the driver
    wing_morphing = 2 : wing span is the driver
    """
    wing_morphing_i = 1
    return wing_morphing_i

#===========================================================================================================
def hld_type(n_pax_ref):
    """
    hld_type = 0  : Clean
    hld_type = 1  : Flap only, Rotation without slot
    hld_type = 2  : Flap only, Rotation with slot      (ATR)
    hld_type = 3  : Flap only, Rotation double slot
    hld_type = 4  : Flap only, Fowler
    hld_type = 5  : Slap only
    hld_type = 6  : Slat + Flap rotation double slot
    hld_type = 7  : Slat + Flap rotation with slot
    hld_type = 8  : Slat + Flap rotation double slot
    hld_type = 9  : Slat + Fowler                      (A320)
    hld_type = 10 : Slat + Slotted Fowler (A321)
    """
    if (n_pax_ref>100):
        hld_type_i = 9
    else:
        hld_type_i = 7
    return hld_type_i

#===========================================================================================================
def wing_area(n_pax_ref,design_range):
    wing_area_i = 60 + 88*n_pax_ref*design_range*1e-9
    return wing_area_i

#===========================================================================================================
def hld_conf_clean():
    hld_conf_clean_i = 0        # By definition (0=<hld_conf=<1)
    return hld_conf_clean_i

#===========================================================================================================
def hld_conf_ld():
    hld_conf_ld_i = 1       # by definition (0=<hld_conf=<1)
    return hld_conf_ld_i

#===========================================================================================================
def wing_aspect_ratio():
    wing_aspect_ratio_i = 9
    return wing_aspect_ratio_i

#===========================================================================================================
def wing_span(wing_area,wing_aspect_ratio):
    wing_span_i = numpy.sqrt(wing_area*wing_aspect_ratio)
    return wing_span_i

#===========================================================================================================
def wing_sweep(cruise_mach):
    wing_sweep_i = 1.6*max(0,(cruise_mach-0.5))     # Empirical law
    return wing_sweep_i

#===========================================================================================================
def wing_mac(wing_area_i,wing_aspect_ratio_i):
    wing_mac_i = 1.2*numpy.sqrt(wing_area_i / wing_aspect_ratio_i)
    return wing_mac_i


#===========================================================================================================
def fuel_type():
    fuel_type_i = 1     # 1: kerosene, 2: hydrogene
    return fuel_type_i

#===========================================================================================================
def nacelle_body_length():
    nacelle_body_length_i = 4
    return nacelle_body_length_i

#===========================================================================================================
def nacelle_body_width():
    nacelle_body_width_i = 1.5
    return nacelle_body_width_i

#===========================================================================================================
def nacelle_body_hub_width():
    nacelle_body_hub_width_i = 0.5
    return nacelle_body_hub_width_i

#===========================================================================================================
def nacelle_attachment(n_pax_ref):
    if (80<n_pax_ref):
        nacelle_attachment_i = 1     # 1: underwing
    else:
        nacelle_attachment_i = 2     # 2: on rear fuselage
    return nacelle_attachment_i

#===========================================================================================================
def efficiency_fan():
    efficiency_fan_i = 0.95     # efficiency to convert shaft power into kinetic energy
    return efficiency_fan_i

#===========================================================================================================
def efficiency_prop():
    efficiency_prop_i = 0.82     # efficiency of a fan to convert shaft power into propulsive power
    return efficiency_prop_i

	
#===========================================================================================================
def propeller_efficiency():
    propeller_efficiency_i = 0.85     # efficiency of a propeller to convert shaft power into propulsive power
    return propeller_efficiency_i


#===========================================================================================================
def n_engine():
    n_engine_i = 2
    return n_engine_i

#===========================================================================================================
def bpr(n_pax_ref):
    if (80<n_pax_ref):
        bpr_i = 9
    else:
        bpr_i = 5
    return bpr_i

#===========================================================================================================
def reference_thrust(n_pax_ref,design_range,n_engine):
    reference_thrust_i = (1e5 + 177*n_pax_ref*design_range*1e-6)/n_engine
    return reference_thrust_i

#===========================================================================================================
def turbofan_nacelle_width(bpr,reference_thrust):
    turbofan_nacelle_width_i = 0.5 * bpr ** 0.7 + 5E-6 * reference_thrust
    return turbofan_nacelle_width_i

#===========================================================================================================
def turbofan_nacelle_y_ext(attachment,fuselage_width_i,nacelle_width_i):
    if attachment == 1 :
        nacelle_y_ext_i = 0.7 * fuselage_width_i + 1.5 * nacelle_width_i
    else:
        nacelle_y_ext_i = 0.5 * fuselage_width_i + 0.5 * nacelle_width_i
    return nacelle_y_ext_i

#===========================================================================================================
def core_thrust_ratio():
    core_thrust_ratio_i = 0.13    # Mean contribution of the core to the total thrust
    return core_thrust_ratio_i

#===========================================================================================================
def core_width_ratio():
    core_width_ratio_i = 0.70    # Ratio of core mean diameter over fan diameter
    return core_width_ratio_i

#===========================================================================================================
def core_weight_ratio():
    core_weight_ratio_i = 0.13    # Mean contribution of the core to the total engine weight
    return core_weight_ratio_i

	
#===========================================================================================================
def prop_architecture():
    prop_architecture_i = 1    # prop_architecture, 1: turbofan, 2: partial turbo electric
    return prop_architecture_i

#===========================================================================================================
def electric_shaft_power():
    electric_shaft_power_i = 1e6    # Watts, electric motor power
    return electric_shaft_power_i

#===========================================================================================================
def battery_strategy():
    battery_strategy_i = 1    # Battery sizing strategy, 1: power_feed & energy_cruise driven, 2: battery mass driven
    return battery_strategy_i

#===========================================================================================================
def battery_power_feed():
    battery_power_feed_i = 0.    # Power delivered to e-fan(s) at take off and(or) climb during a total of time_feed
    return battery_power_feed_i

#===========================================================================================================
def battery_time_feed():
    battery_time_feed_i = unit.s_min(15)    # Maximum duration of the power_feed delivered to e-fan(s)
    return battery_time_feed_i

#===========================================================================================================
def battery_energy_cruise():
    battery_energy_cruise_i = 0.    # Total battery energy dedicated to cruise
    return battery_energy_cruise_i

#===========================================================================================================
def battery_energy_density():
    battery_energy_density_i = unit.J_kWh(0.2)    # Battery energy density
    return battery_energy_density_i

#===========================================================================================================
def battery_power_density():
    battery_power_density_i = 1e3    # Battery power density (capability to release power per mass unit
    return battery_power_density_i

#===========================================================================================================
def e_chain_efficiency():
    e_chain_efficiency_i = 0.90    # Overall efficiency of the electric chain, from generator to motor
    return e_chain_efficiency_i

#===========================================================================================================
def controller_efficiency():
    controller_efficiency_i = 0.98    # no_dim
    return controller_efficiency_i

#===========================================================================================================
def e_motor_efficiency():
    motor_efficiency_i = 0.98    # no_dim
    return motor_efficiency_i

#===========================================================================================================
def generator_power_density():
    generator_power_density_i = 10e3    # W/kg, Electric generator
    return generator_power_density_i

#===========================================================================================================
def rectifier_pw_density():
    rectifier_pw_density_i = 20e3    # W/kg, Rectifier
    return rectifier_pw_density_i

#===========================================================================================================
def wiring_pw_density():
    wiring_pw_density_i = 20e3    # W/kg, Wiring
    return wiring_pw_density_i

#===========================================================================================================
def cooling_pw_density():
    cooling_pw_density_i = 15e3    # W/kg, Cooling
    return cooling_pw_density_i

#===========================================================================================================
def controller_pw_density():
    controller_pw_density_i = 20e3    # W/kg, Electric motor
    return controller_pw_density_i

#===========================================================================================================
def e_motor_pw_density():
    e_motor_pw_density_i = 10e3    # W/kg, Electric motor
    return e_motor_pw_density_i

#===========================================================================================================
def e_nacelle_pw_density():
    e_nacelle_pw_density_i = 5e3    # W/kg, Electric nacelle
    return e_nacelle_pw_density_i

#===========================================================================================================
def boundary_layer_effect():
    bli_effect_i = 1    # 0: without, 1: with
    return bli_effect_i


#===========================================================================================================
def htp_attachment(nacelle_attachment_i):
    if (nacelle_attachment_i == 1):
        htp_attachment_i = 1        # 1: Classical (on fuselage tail cone)
    else:
        htp_attachment_i = 2        # 2: T-tail (on top of fin)
    return htp_attachment_i


#===========================================================================================================
def mtow(n_pax_ref,design_range):
    mtow_i =  20500 + 67e-6*n_pax_ref*design_range
    return mtow_i

#===========================================================================================================
def mzfw(n_pax_ref,design_range):
    mzfw_i = 25000 + 41e-6*n_pax_ref*design_range
    return mzfw_i

#===========================================================================================================
def mlw(n_pax_ref,mtow_i,mzfw_i):
    if (n_pax_ref>100):
        mlw_i = min(mtow_i , (1.07*mzfw_i))
    else:
        mlw_i = mtow_i
    return mlw_i


#===========================================================================================================
def disa_oei():
    init_disa_oei_i = 15
    return init_disa_oei_i

#===========================================================================================================
def req_oei_altp(propulsive_architecture):
    req_oei_altp_i = unit.m_ft(11000)
    return req_oei_altp_i


#===========================================================================================================
def altp_tofl():
    altp_tofl_i = 0
    return altp_tofl_i

#===========================================================================================================
def disa_tofl():
    disa_tofl_i = 15
    return disa_tofl_i

#===========================================================================================================
def req_tofl(design_range):
    if(design_range <= unit.m_NM(3500)):
        req_tofl_i = 2000
    elif(design_range <= unit.m_NM(5500)):
        req_tofl_i = 2500
    else:
        req_tofl_i = 3000
    return req_tofl_i


#===========================================================================================================
def altp_app_speed():
    altp_app_speed_i = unit.m_ft(0)
    return altp_app_speed_i

#===========================================================================================================
def disa_app_speed():
    disa_app_speed_i = 0
    return disa_app_speed_i

#===========================================================================================================
def req_app_speed(n_pax_ref):
    if (n_pax_ref<=100):
        req_app_speed_i = unit.mps_kt(135)
    elif (n_pax_ref<=200):
        req_app_speed_i = unit.mps_kt(137)
    else:
        req_app_speed_i = unit.mps_kt(140)
    return req_app_speed_i


#===========================================================================================================
def cas1_ttc(cruise_mach):
    if (cruise_mach>=0.6):
        cas1_ttc_i = unit.mps_kt(250)
    else:
        cas1_ttc_i = unit.mps_kt(190)
    return cas1_ttc_i

#===========================================================================================================
def cas2_ttc(cruise_mach):
    if (cruise_mach>=0.6):
        cas2_ttc_i = unit.mps_kt(300)
    else:
        cas2_ttc_i = unit.mps_kt(240)
    return cas2_ttc_i

#===========================================================================================================
def req_ttc():
    req_ttc_i = unit.s_min(25)
    return req_ttc_i


#===========================================================================================================
def disa_climb():
    disa_climb_i = 15
    return disa_climb_i

#===========================================================================================================
def req_vz_climb():
    req_vz_climb_i = unit.mps_ftpmin(300)
    return req_vz_climb_i

#===========================================================================================================
def req_vz_cruise():
    req_vz_cruise_i = unit.mps_ftpmin(0)
    return req_vz_cruise_i

	
#===========================================================================================================
def cost_mission_disa():
    cost_mission_disa_i = 0
    return cost_mission_disa_i

#===========================================================================================================
def cost_mission_range(design_range):
    if(design_range < unit.m_NM(4500)): cost_mission_range_i = unit.m_NM(800)
    elif(design_range < unit.m_NM(6500)): cost_mission_range_i = unit.m_NM(2000)
    else:                               cost_mission_range_i = unit.m_NM(4000)
    return cost_mission_range_i

def fuel_price():
#===========================================================================================================
    fuel_price_i = 2/unit.liter_usgal(1)   # 2 $/USgal
    return fuel_price_i

def elec_price():
#===========================================================================================================
    elec_price_i = 0.15/unit.J_kWh(1)   # 0.15 $/kWh  Assumed de-carbonated
    return elec_price_i

def battery_price():
#===========================================================================================================
    battery_price_i = 20   # $/kg    installed
    return battery_price_i

#===========================================================================================================
def labor_cost():
    labor_cost_i = 120   # 120 $/h
    return labor_cost_i

#===========================================================================================================
def irp():
    irp_i = 10     # 10 years
    return irp_i

#===========================================================================================================
def period():
    period_i = 15     # 15 years
    return period_i

#===========================================================================================================
def interest_rate():
    interest_rate_i = 0.04     # 4%
    return interest_rate_i

#===========================================================================================================
def utilisation(design_range):
    if(design_range <= unit.m_NM(3500)): utilisation_i = 1600
    else:                                utilisation_i = 600
    return utilisation_i

