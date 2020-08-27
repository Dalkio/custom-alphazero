import os

gpu_index = "-1"
tensorflow_log_level = "3"
os.environ["CUDA_VISIBLE_DEVICES"] = gpu_index
os.environ["TF_CPP_MIN_LOG_LEVEL"] = tensorflow_log_level


class ConfigGeneral:
    game = "connect_n"
    concurrency = True
    mono_process = False
    discounting_factor = 1  # set to 1 to actually disable any discounting effect
    mcts_iterations = 75
    minimum_training_size = 2500
    minimum_delta_size = 1000
    samples_queue_size = 10000
    training_iterations = 10000
    run_with_http = False


class ConfigChess:
    piece_symbols = [None, "p", "n", "b", "r", "q", "k"]
    initial_board_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    initial_turn = "w"
    initial_castling_rights = "KQkq"
    initial_ep_quare = "-"
    initial_halfmove_clock = "0"
    initial_fullmove_number = "1"
    board_size = 8
    number_unique_pieces = 12


class ConfigConnectN:
    board_width = 7
    board_height = 6
    n = 4
    gravity = True
    black = -1
    empty = 0
    white = 1
    pieces = {-1: "O", 0: ".", 1: "X"}
    directions = [(0, 1), (1, 1), (1, 0), (1, -1)]


class ConfigMCTS:
    exploration_constant = 1.5
    enable_dirichlet_noise = False  # disabled for now
    dirichlet_noise_value = 0.03
    dirichlet_noise_ratio = 0.25
    index_move_greedy = 8  # 30 should be the default value
    use_solver = False


class ConfigModel:
    model_suffix = "model"
    model_meta = "meta.json"
    l2_penalization_term = 1e-4
    depth = 2
    maximum_learning_rate = 1e-2
    learning_rates = {
        range(0, 150000): 1e-2,
        range(150000, 300000): 1e-3,
    }
    minimum_learning_rate = 1e-4
    momentum = 0.9
    filters = 128


class ConfigServing:
    serving_host = "localhost"
    serving_port = 5000
    serving_address = "http://{0}:{1}".format(serving_host, serving_port)
    """
    import multiprocessing
    # seems not to run as fast as expected for now
    inference_batch_size = multiprocessing.cpu_count() - 1
    """
    inference_batch_size = 1
    inference_timeout = 1
    model_checkpoint_frequency = 1
    samples_checkpoint_frequency = 1
    training_epochs = 25
    batch_size = 256
    evaluation_games_number = 100
    replace_min_score = 0.55
    evaluate_with_mcts = False
    evaluate_with_solver = True


class ConfigPath:
    inference_path = "/api/inference"
    training_path = "/api/training"
    results_path = "results"
    samples_name = "samples.npz"
    saved_inferences_name = "state_priors_value.pkl"
    updated_mcts_dir = "updated_mcts"
    tensorboard_endpath = "tensorboard"
    mcts_visualization_endpath = "mcts_visualization"
    connect4_solver_path = "./src/exact_solvers/c4solver"
    connect4_opening_book = "./src/exact_solvers/7x6.book"
