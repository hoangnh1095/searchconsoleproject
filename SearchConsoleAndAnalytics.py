import tkinter as tk
import sys
from googleapiclient import sample_tools

HEIGHT=500
WIDTH=600

#key_APi : AIzaSyBvlz3Z0NFJNg3FVUA2GCIobZ9rxsAy_CY
#Client_ID : 300198945990-tbtlf8fp93qmhkvco0q6q2ecdnal5voe.apps.googleusercontent.com
#Client_secret : 7umacvRGJP5RaSLMC_fJ4-2L


root=tk.Tk()


canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

#background_image=tk.PhotoImage(file='bg.png')
#background_label=tk.Label(root,image=background_image)
#background_label.place(x=0,y=0,relwidth=1,relheight=1)

#function

def getData(inputData):
    service, flags = sample_tools.init( "", 'webmasters', 'v3', __doc__, __file__, parents=[inputData],scope='https://www.googleapis.com/auth/webmasters.readonly')

def test_button(entry):
    inputData=["https://vixlinh.000webhostapp.com","2020-09-01","2020-09-30"]
    

def execute_request(service, property_uri, request):
  return service.searchanalytics().query(siteUrl=property_uri, body=request).execute()

def print_table(response, title):
  """Prints out a response table.
  Each row contains key(s), clicks, impressions, CTR, and average position.
  Args:
    response: The server response to be printed as a table.
    title: The title of the table.
  """
  print('\n --' + title + ':')
  
  if 'rows' not in response:
    print('Empty response')
    return

  rows = response['rows']
  row_format = '{:<20}' + '{:>20}' * 4
  print(row_format.format('Keys', 'Clicks', 'Impressions', 'CTR', 'Position'))
  for row in rows:
    keys = ''
    # Keys are returned only if one or more dimensions are requested.
    if 'keys' in row:
      keys = u','.join(row['keys']).encode('utf-8').decode()
    print(row_format.format(
        keys, row['clicks'], row['impressions'], row['ctr'], row['position']))


#frame1
frame = tk.Frame(root, bg='#00b3b3',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button= tk.Button(frame,text="Hello World!!!",bg="white",font=40,command=lambda : test_button(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)

#frame2
lower_frame = tk.Frame(root, bg='#00b3b3',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label= tk.Label(lower_frame)
label.place(relwidth=1,relheight=1)

root.mainloop()



