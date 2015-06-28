import os

os.system("echo \"\nWelcome to Bret\'s interactive awscli program!\n\n\"")
while True:
  os.system("echo \"please select an option below:\n\"")
  os.system("echo \"1.) List servers\n2.) Stop server(s)\n3.) Start server(s)\n4.) Restart server(s) on new host\n5.) Launch nser server(s)\n6.) Terminate server(s)\n7.) Exit Program\"")
  main_selection = raw_input()
  if main_selection.strip() == '7':
    break
  elif main_selection.strip() == '1':
      os.system("aws ec2 describe-instances --output table")
