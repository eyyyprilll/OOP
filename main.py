# FUTURE ME 
# March 16, 2024
# This program collects your name and your dream job.


def print_fancy(name, dream_job):
    header = "*******************************"
    content = [
        f"* Name: {name.ljust(26)}",
        f"*Dream Job {dream_job.ljust(19)}"
    ]
    print("\033[1m\033[95m" + header)
    for line in content: 
        print(line)
    print(header +  "\033[0m")
    
def main():
    name = input ("Enter your name: ")
    dream_job = input ("Enter your dream job: ")
    print_fancy(name, dream_job)
    
if __name__=="__main__":
    main()