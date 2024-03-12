"""
Linux 'tree' but for Python
"""

# %% Modules

from colorama import Fore

# %% Global variables

BRANCH    = "├── "
SEPARATOR = "│   "
CLOSING   = "└── "
SPACING   = "    "
TEMP = None

# %% Modules

def tree(dictionary, node_name, max_depth = None, datatypes = True, depth = 0, fill = ""):
    """
    Build the tree representation of a dictionary and its children

    Input parameters:
    - dictionary <dict>: Dictionary to be used to create the tree
    - node_name <str>: Name of the dictionary to be uses as the root node
    - max_depth <int>: Maximum depth of the tree to be printed (e.g., 'max_depth = 0' only prints the root, 'max_depth = 1' prints the root and its immediate children)
    - datatypes <bool>: Print the datatype of the leaf nodes in the tree (i.e., nodes at 'max_depth' are considered leaf nodes)
    """

    # If 'max_depth = 0', return the name of the root node

    if isinstance(max_depth, int) and max_depth == 0:
        if datatypes:
            return "%s%s:%s %s<dict>%s\n" % (Fore.GREEN, node_name, Fore.WHITE, Fore.RED, Fore.WHITE)
        else:
            return "%s%s%s" % (Fore.GREEN, node_name, Fore.WHITE)

    # Initialize output

    global TEMP

    if TEMP == None:
        TEMP = ""

    # Print the name of the root node

    if depth == 0:
        TEMP += Fore.GREEN + node_name + Fore.WHITE + "\n"

    # Return if maximum depth is reached

    if depth == max_depth:
        return 

    # Make sure the input is a dictionary

    assert isinstance(dictionary, dict), "Argument passed MUST be a dictionary"

    # Print children and recurse if necessary

    num_keys = len(dictionary)
    kdx = 0

    for key, value in dictionary.items():
        TEMP += fill

        if kdx == num_keys - 1:
            TEMP += CLOSING
        else:
            TEMP += BRANCH

        if isinstance(value, dict):
            if max_depth == None or depth < max_depth - 1:
                TEMP += "%s%s%s\n" % (Fore.GREEN, key, Fore.WHITE)
                tree(value, node_name, max_depth, datatypes = datatypes, fill = fill + SEPARATOR if kdx < num_keys - 1 else fill + SPACING, depth = depth + 1)
            else:
                if datatypes:
                    TEMP += "%s%s:%s %s<dict>%s\n" % (Fore.GREEN, key, Fore.WHITE, Fore.RED, Fore.WHITE)
                else:
                    TEMP += "%s%s%s\n" % (Fore.GREEN, key, Fore.WHITE)

        else:
            if datatypes:
                TEMP += "%s%s:%s <%s>%s\n" % (Fore.BLUE, key, Fore.RED, type(value).__name__, Fore.WHITE)
            else:
                TEMP += "%s%s%s\n" % (Fore.BLUE, key, Fore.WHITE)

        kdx += 1

    if depth == 0:
        output = str(TEMP)
        TEMP = None
        return output
    else:
        return

# % Testing

if __name__ == "__main__":
    dictionary = {}
    dictionary["data"] = {}
    dictionary["data"]["ab_dataset"] = None
    dictionary["data"]["check_dataset"] = None
    dictionary["data"]["examples"] = None
    dictionary["features"] = {}
    dictionary["features"]["config"] = {}
    dictionary["features"]["config"]["dense_diffmasif_example"] = None
    dictionary["features"]["config"]["dense_diffmasif_features"] = None
    dictionary["features"]["config"]["example"] = None
    dictionary["features"]["config"]["pair_feature_defaults"] = None
    dictionary["features"]["config"]["residue_feature_defaults"] = None
    dictionary["features"]["config"]["sparse_diffmasif_example"] = None
    dictionary["features"]["config"]["sparse_diffmasif_features"] = None
    dictionary["features"]["examples"] = None
    dictionary["features"]["test_diffmasif_binding_model"] = None
    dictionary["features"]["test_diffmasif_features"] = None
    dictionary["features"]["test_diffmasif_transforms"] = None
    dictionary["loss"] = {}
    dictionary["loss"]["Untitled"] = None
    dictionary["masking"] = {}
    dictionary["masking"]["test_mask_gens"] = 5
    dictionary["model"] = {}
    dictionary["model"]["dockgpt"] = {}
    dictionary["model"]["dockgpt"]["dockgpt_ga_stats"] = None
    dictionary["model"]["dockgpt"]["test_tri_mul"] = None
    dictionary["model"]["docking"] = {}
    dictionary["model"]["docking"]["docking_stats"] = None
    dictionary["model"]["latent_diffusion"] = {}
    dictionary["model"]["latent_diffusion"]["Check_OOD_Examples"] = None
    dictionary["model"]["latent_diffusion"]["Diffusion_Inference"] = None
    dictionary["model"]["latent_diffusion"]["vae_inference"] = None
    dictionary["model"]["neodiff"] = {}
    dictionary["model"]["neodiff"]["generate_cluster_data"] = None
    dictionary["model"]["neodiff"]["neodiff-ipa_tests"] = None
    dictionary["model"]["neodiff"]["tests_for_ipa_chain"] = None
    dictionary["transforms"] = {}
    dictionary["transforms"]["generate_cluster_data_1"] = None
    dictionary["transforms"]["generate_cluster_data_2"] = None
    dictionary["transforms"]["check_transform_compatibility"] = None

    name = "notebooks"
    print(tree(dictionary, name))

# %% End of script
