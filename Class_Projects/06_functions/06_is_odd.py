def main():
        for i in range(10):
            if is_odd (i): 
              print('even')
            else:
                print('odd')
def is_odd(value:int):
    """Checks to see if value is odd.If it is returns true"""
    remainder=value%2 # 0 if value is divisible by 2, 1 if it isn't.
    return remainder==1
if __name__ == '__main__':
    main()