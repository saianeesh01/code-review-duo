import sys
from crewai_app.agents.reviewer import ReviewBot
from crewai_app.agents.fixer import FixBot

def main():
    # Example CLI entrypoint
    print("Starting code review...")
    reviewer = ReviewBot()
    fixer = FixBot()
    reviewer.run()
    fixer.run()

if __name__ == "__main__":
    main()
