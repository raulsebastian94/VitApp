import datetime



med_list = []


class Medication:

    def __init__(self, rx_name=None, rx_number=None, rx_strength=None, rx_unit=None, rx_instructions=None,\
                 rx_physical_description=None, rx_discard_after_date=None, rx_date_written=None, rx_date_filled=None,\
                 rx_date_refill_avail=None, rx_quantity_remain=None, rx_quantity_filled=None,pharmacy_name=None,\
                 pharmacy_phone_num=None, doctor=None):

        self.rx_name = rx_name
        self.rx_number = rx_number
        self.rx_strength = rx_strength
        self.rx_unit = rx_unit
        self.rx_instructions = rx_instructions
        self.rx_physical_description = rx_physical_description
        self.rx_discard_after_date = rx_discard_after_date
        self.rx_date_written = rx_date_written
        self.rx_date_filled = rx_date_filled
        self.rx_date_refill_avail = rx_date_refill_avail
        self.rx_quantity_filled = rx_quantity_filled
        self.rx_quantity_remain = rx_quantity_remain
        self.pharmacy_name = pharmacy_name
        self.pharmacy_phone_num = pharmacy_phone_num
        self.doctor = doctor


    def user_name(self):

        self.rx_name = input("RX Name: ")

    def user_number(self):

        self.rx_number = input("RX Number: ")


    def user_strength(self):

        self.rx_strength = input("RX Strength(Numbers only eg: .5, 1, 1000, etc): ")

    def user_unit(self):

        self.rx_unit = input("Unit of Measurement(mg, g, etc): ")

    def user_nstructions(self):

        self.rx_instructions = input("RX Instructions: ")

    def user_phys_desc(self):

        self.rx_physical_description = input("Physical Description: ")

    def user_disc_date(self):

        self.rx_discard_after_date = input("Discard after date: ")

    def user_date_writ(self):

        self.rx_date_written = input("Date Written: ")

    def user_date_fill(self):

        self.rx_date_filled = input("Date filled: ")

    def user_date_refl_aval(self):

        self.rx_date_refill_avail = input ("Date refill available: ")

    def user_q_filled(self):

        self.rx_quantity_filled = input("Quantity filled: ")

    def user_q_remain(self):

        self.rx_quantity_remain = input("Quantity remain: ")

    def user_pharm(self):

        self.pharmacy_name = input("Pharmacy Name: ")
        self.pharmacy_phone_num = input("Pharmacy Phone Number")

    def user_doctor(self):

        self.doctor = input("RX prescribing Doctor: ")


def user_med_info():

    global x
    x = Medication()
    x.user_name()
    x.user_number()
    x.user_strength()
    x.user_unit()
    x.user_nstructions()
    x.user_phys_desc()
    x.user_disc_date()
    x.user_date_writ()
    x.user_date_fill()
    x.user_date_refl_aval()
    x.user_q_filled()
    x.user_q_remain()
    x.user_pharm()
    x.user_doctor()




def write_dictionary():
    dict = {'Name': x.rx_name, 'Rx Number': x.rx_number, 'RX Strength': x.rx_strength, 'Units', x.rx_unit,\
            }

user_med_info()











