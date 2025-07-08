#objective:Manage a collection of books that users can borrow and return.
from library_utils import check_filepath

check_filepath()

def management_system():
    from library_utils import menu
    from library_utils import read_write_library_book_json
    read_write_library_book_json()
    while True:
        options = menu()
        if options == 1:
            from library_utils import add_option
            add_option()
        elif options == 2:
            from library_utils import borrow_option
            borrow_option()
        elif options == 3:
            from library_utils import return_option
            return_option()
        elif options == 4:
            from library_utils import view_option
            view_option()
        elif options == 5:
            print("your records are save, ensure you don't delete the json file written into your disk, and you can continue from where you stopped anytime")
            break


management_system()

