
#Import Modules
import random

#Global constants
COMPANY_NAME = 'Victorino County Tax Assessor'
DISPLAY_MAX_WIDTH = 70
INDENT_1 = ' '*3
INDENT_2 = ' '*5
INDENT_3 = ''
BAR_1 = '*'*79
BAR_2 = '-'*70

application_name = 'Residential Property Tax Estimation Tool'


#MAIN-------------------------------------------------------------------------------------
def main():

    #Initialize constants & variables
    APPLICATION_NAME = 'Residential Property Tax Estimation Tool'
    avg_home_value = 130
    price_per_acre = 43560
    market_value_per_acre = 100000
    property_tax = 0.02
    #property_tax_value = property_value * property_tax

    #Display headers
    display_company_banner()
    display_welcome_message(application_name)

    #INPUT-----------------------------------------------------
    property_address = input(INDENT_1 + 'Enter Property Address: ')
    building_size = int(input(INDENT_1 + 'Enter Building Size (sqft): '))
    front = float(input(INDENT_1 + 'Enter Land Effective Front (ft): '))
    depth = float(input(INDENT_1 + 'Enter Land Effective depth (ft): '))
    exemption_code = input(INDENT_1 + 'Enter Exemption Code - (H)omestead, (O)ver 65, or (N)one: ').lower()
    get_exemption_name(exemption_code)
    print()

    #PROCESS---------------------------------------------------
    print(f'{BAR_2:^79}')
    print(f'{"Property Tax Estimate Report":^70}')
    print(f'{BAR_2:^79}')
    print()
    
    #OUTPUT----------------------------------------------------
    print(INDENT_1 + '>>>> Report for Property Located at: ', property_address)
    print()
    print(INDENT_1 + 'Building: ', f'{building_size} sqft')
    print()
    print(INDENT_1 + 'Land Info')
    print(f'{INDENT_2}Front: {front:>9.2f}  \t  Depth: {depth:<15.2f}')

    total_square_footage = front * depth
    total_acres = total_square_footage / price_per_acre
    print(f'{INDENT_2}Sqft: {calc_land_square_footage(front, depth):>10,.2f}  \t  {INDENT_3}Acres: {calc_land_acres(calc_land_square_footage(front, depth), price_per_acre):<15.4f}')
    print()

    bldg_mkt_value = avg_home_value * building_size
    print(f'{INDENT_1}Building Market Value: {INDENT_1}{INDENT_2}{calc_bldg_value(avg_home_value, building_size):>10,.2f}')

    land_market_value = total_acres * market_value_per_acre
    print(f'{INDENT_1}Land Market Value: {INDENT_1}{INDENT_2}{calc_land_market_value(total_acres, \
        market_value_per_acre):>14,.2f}')

    property_value = bldg_mkt_value + land_market_value
    property_tax_value = property_value * property_tax
    bldg_mkt_value = avg_home_value * building_size
    
    exemption_name = get_exemption_name(exemption_code)
    print(
    f'{INDENT_1}Taxes w/Current Exemptions: ' 
    f'{INDENT_1}{calc_property_taxes(property_value, bldg_mkt_value, \
        land_market_value, property_tax, exemption_name):>10,.2f}'
    f' ({exemption_code.upper()} - {exemption_name})')

    
    print(f'{INDENT_1}Taxes w/o Exemptions: {INDENT_1}{INDENT_2}{property_tax_value:>11,.2f}')

    print(f'{INDENT_1}{BAR_2}')

    con_num = random.randrange(1, 1000000, 1)
    print(f'{INDENT_1}{"Confirmation No: "} {gen_confirmation_no()}') 
   
#FUNCTIONS--------------------------------------------------------------------------------

#FN1: Company banner
def display_company_banner():
    print()
    print(BAR_1)
    print(f'{COMPANY_NAME:^69}')
    print(BAR_1)
    print()
    

#FN2: Welcome message
def display_welcome_message(application_name):
    print(f"{'Welcome to the ' + application_name + '!':^69}")
    print()

#FN3: Exemption name
def get_exemption_name(exemption_code):
    if exemption_code == 'h':
        return 'Homestead'
    elif exemption_code == 'o':
        return 'Over 65'
    else:
        return 'None'

#FN4: Building value
def calc_bldg_value(avg_home_value, building_size):
    bldg_mkt_value = avg_home_value * building_size
    return bldg_mkt_value

#FN5: Land sqft
def calc_land_square_footage(front, depth):
    total_square_footage = front * depth
    return total_square_footage

#FN6: Land acres
def calc_land_acres(total_square_footage, price_per_acre):
    total_acres = total_square_footage / price_per_acre
    return total_acres

#FN7: Land value
def calc_land_market_value(total_acres, market_value_per_acre):
    land_market_value = market_value_per_acre * total_acres
    return land_market_value

#FN8: Property taxes
def calc_property_taxes(property_value, bldg_mkt_value, land_market_value, property_tax, exemption_name):
    property_value = bldg_mkt_value + land_market_value
    property_tax_value = property_value * property_tax

    if exemption_name == 'Homestead':
        property_tax_value *= 0.85
    elif exemption_name == 'Over 65':
        property_tax_value *= 0.80

    return property_tax_value
        
#FN9: Confirmation number
def gen_confirmation_no():
    con_num = random.randrange(100000, 1000000, 1)
    return con_num
  
#FN10: isfloat()
def isfloat(value):
    try: 
        float(value) 
        return True
    except: 
        return False

main() 



