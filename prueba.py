def say_hello( name: str ) -> None:
    print( f"Hello, {name}!" )

def even_or_odd( number: int ) -> None:
    if number % 2 == 0:
        print( f"{number} is even" )
    else:
        print( f"{number} is odd" )

if __name__ == "__main__":
    say_hello( "Leonel" )
    user_number = int( input( "Enter a number: " ) )
    even_or_odd( user_number )