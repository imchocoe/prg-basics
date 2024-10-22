def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inches(n):
    return n/2.54

def feet_to_cm(n):
    return n*457.2



if __name__ == "__main__":
    # only execute when you run this module
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f"576cm={cm_to_inches(576)}in")
    print(f"32.5feet={feet_to_cm(32.5)}cm")

    