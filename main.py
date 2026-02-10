if __name__ == '__main__':
    print("Agent Kecil: Starting...")
    # Initialize Diplomat
    diplomat = Diplomat()
    diplomat.setup()

    # Initialize Penjelajah
    penjelajah = Penjelajah()
    penjelajah.start_exploration()

    print("Agent Kecil: Orchestration complete.")