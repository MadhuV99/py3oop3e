# augmented_move.py 

import shutil
import os.path


def augmented_move(
    target_folder, *filenames, verbose=False, **specific):
    """Move all filenames into the target_folder, allowing
    specific treatment of certain files."""

    def print_verbose(message, filename):
        """print the message only if verbose is enabled"""
        if verbose:
            print(message.format(filename))

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        if filename in specific:
            if specific[filename] == "ignore":
                print_verbose("Ignoring {0}", filename)
            elif specific[filename] == "copy":
                print_verbose("Copying {0}", filename)
                shutil.copyfile(filename, target_path)
        else:
            print_verbose("Moving {0}", filename)
            shutil.move(filename, target_path)

def main():
                # "augmented_move.py", 
                # "custom_sequence.py", 

    # augmented_move(
    #             "move_folder", 
    #             "move_it_1",
    #             "move_it_2",
    #             "move_it_3",
    #             verbose=True,
    #             move_it_1="copy",
    #             move_it_2="ignore"
    #         )

    # some_args = ["move_it_1", "move_it_2", "move_it_3"]
    # more_args = {
    #             "move_it_1": "copy",
    #             "move_it_2": "ignore"
    #             }

    some_args = ["augmented_move.py", "custom_sequence.py", "move_it_3"]
    more_args = {
                "augmented_move.py": "copy",
                "custom_sequence.py": "ignore"
                }

    augmented_move(
                "move_folder", 
                *some_args,
                verbose=True,
                **more_args
            )



if __name__ == '__main__':
    main() 