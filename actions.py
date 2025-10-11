import time
import webbrowser

# perform_actions('Thumb_up')


def perform_actions(gesture: str):
  url = "https://youtube.com"
  print(f"gesture passed to perform task: {gesture}")
  
  if gesture != 'None':
    match gesture:
      case "Thumb_Up":
        webbrowser.open_new_tab(url)

      case _:
        print(gesture)
  



    