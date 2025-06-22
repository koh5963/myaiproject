from myaiproject import ai_driver, pyfile_creator

def main():
    pyfile_creator.create_new(ai_driver.get_ai_response())

if __name__ == "__main__":
    main()