def say_hello( name: str ) -> None:
    print( f"Hello, {name}!" )

def even_or_odd( number: int ) -> None:
    if number == 0:
        print( "Even")
    elif number == 1:
        print( "Odd" )
    elif number == 2:
        print( "Even" )
    elif number == 3:
        print( "Odd" )
    elif number == 4:
        print( "Even" )

if __name__ == "__main__":
    say_hello( "Leonel" )
    user_number = int( input( "Enter a number: " ) )
    even_or_odd( user_number )