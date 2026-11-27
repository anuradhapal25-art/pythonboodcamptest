# import time

# def timer_dec(base_fn):
#     def enhanced_fn():
#         start_time = time.time()
#         base_fn()
#         end_time = time.time()
#         print(f"Task time: {end_time - start_time} seconds")

#     return enhanced_fn


# @timer_dec
# def make_tea():
#     print("Brewing tea...")
#     time.sleep(1)
#     print("Tea is ready!")


# @timer_dec
# def make_coffee():
#     print("Making coffee...")
#     time.sleep(1)
#     print("Coffee is ready!")


# make_tea()
# make_coffee()

import time

def timer_dec(base_fn):
    def enhanced_fn():
        start_time = time.time()
        base_fn()
        end_time = time.time()
        print(f"Enhance function - Task time: {end_time - start_time} seconds")

    return enhanced_fn


@timer_dec
def make_tea():
    print("Brewing tea...")
    time.sleep(1)
    print("Tea is ready!")


@timer_dec
def make_coffee():
    print("Making coffee...")
    time.sleep(1)
    print("Coffee is ready!")


make_tea()
