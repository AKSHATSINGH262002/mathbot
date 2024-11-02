import streamlit as st
from PIL import Image
from pytesseract import pytesseract 
import  matplotlib.pyplot as plt
import numpy as np
import pre
import pandas as pd
import company as cp
from pathlib import Path
import time
import mapping as mp


flag=0
img=Image.open('MATHION.png')
st.set_page_config(page_title="MATH-BOT",page_icon=img)

st.title("--MATHEMATICS-BOT--")
#st.header("HOW CAN I HELP YOU FRIEND ?")
st.logo('MATHION.png')
st.sidebar.title("Hiii ! select your option here")
st.header("hello let me work with you",divider="red")
with st.spinner('Wait for it...'):
                time.sleep(5)
st.success('START YOUR WORK')

#if st.sidebar.button("Data_analysis"):

upload=st.sidebar.file_uploader(label="DATA ANALYSIS",type=["xlsx","csv","txt"])
if upload is not None:
        if upload.type=='csv':
                
                df=cp.csv_find(upload)
                st.dataframe(df)
            
        else:
            st.header("--HERE IS YOUR DATAFRAME--")
            df=cp.company_analyse(upload)
            st.dataframe(df)
                  
            clist=mp.graph_data(df)
            ct=st.sidebar.selectbox("select column",clist,index=None)
            if ct is not None:
                l=cp.maths(df,ct)
                st.header("--standard deviation--")
                st.title(l[0])
                st.header("--mean--") 
                st.title(l[1])
                st.header("--median--") 
                st.title(l[2])
                st.header("--mode--")
                st.title(l[3])
            else:
                st.info("choose column from sidebar for mathematical statistics")
                st.info("for graphs see below option")
            
            st.header("--FOR GRAPHS SELECT OPTION--")
            col_list=mp.graph_data(df)
            SELECTED1=st.selectbox("COLUMNS LIST1",col_list,index=None)
            SELECTED2=st.selectbox("COLUMN LIST2",col_list,index=None)
            fig,ax=plt.subplots()
            plt.figure(figsize=(10,6))
            
            if st.button("piechart"):
                  ax.pie(df[SELECTED1],df[SELECTED2],autopct="%0.2f")
                  
                  st.pyplot(fig)
            elif st.button("linear"):
                  ax.plot(df[SELECTED1],df[SELECTED2])
                  
                  st.pyplot(fig)
            if st.button("bar"):  
                    ax.bar(df[SELECTED1],df[SELECTED2])
                    st.pyplot(fig)
        
              
            


uploaded_file=st.sidebar.file_uploader(label="math_solver",type=["jpeg","png","jfif","jpg"])

if uploaded_file is not None:
            
                col1,col2=st.columns(2)
                with col1:
                    image=Image.open(uploaded_file)
                    st.image(image)
                    text=pre.extract(image)
        #arr=text.split()
                    extracted_text=pre.extract(image)
                    d={'extracted_text':extracted_text}
                    df=pd.DataFrame(d)
                    st.dataframe(df)

        
                    if len(extracted_text)==0:
                        st.write("sorry nothing is extracted from image please provide other image \n OR")
            # Display the extracted text
                    ne=st.text_input('ENTER THE FUNCTION YOU WANT')
                    extracted_text.append(ne)
                    st.write("Extracted Text:")
                    st.text(extracted_text) 
            
        #print(arr)
                if st.sidebar.button("EXPLORE"):
                    
                        for i in extracted_text:
    
                            x=np.linspace(0,2*np.pi,100)
                            n=np.linspace(-2 * np.pi, 2 * np.pi, 1000)
                            s=np.linspace(0.1, 10, 1000)
                            t=np.linspace(-2, 2, 1000)
                            if(i=="sin" or i=="Sin"or i=="sin(x)" or i=="sine" or i=="sin x" or i=="SIN"):

                                y_sin=np.sin(x)
                                fig,ax=plt.subplots()
                                ax.plot(x,y_sin,label='sin x',color='red',linewidth=2)
                                plt.xlabel('x')
                                plt.title('sin x graph')
                                st.pyplot(fig)
                    #break
               

                            elif(i=="cos"or i=="Cos" or i=="cos(x)" or i=="cosine"or i=="cosx" or i=="COS"):

                                y_cos=np.cos(x)
                                fig,ax=plt.subplots()
                                ax.plot(x,y_cos,label='cos x',color='red',linewidth=2)
                                plt.xlabel('x')
                                plt.title('cos x graph')
                                st.pyplot(fig)
                    #break
                

    
                            elif(i=="tan"or i=="Tan" or i=="tan(x)" or i=="tangent"or i=="tanx" or i=="TAN"):
                
                                y_tan=np.tan(n)
                                fig,ax=plt.subplots()
                                ax.plot(n,y_tan,label='tan(x)',color='blue')
                                plt.xlabel('x')
                                plt.ylabel('tan(x)')
                                plt.title('tan(x) graph')
                                plt.ylim(-10,10)
                                ax.grid(True)
                                ax.legend()
                                st.pyplot(fig)
                    #break
    
                            elif(i=="cosec"or i=="Cosec" or i=="cosec(x)" or i=="COSEC"):

                                y_cosec=1/np.sin(n)
                                fig,ax=plt.subplots()
                                ax.plot(n,y_cosec,label='cosec(x)',color='green',linewidth=2)
                                plt.xlabel('x')
                                plt.ylabel('cosex(x)')
                                plt.title('cosec(x) graph')
                                plt.ylim(-10,10)
                                st.pyplot(fig)
                    #break

            
                            elif(i=="sec"or i=="Sec" or i=="sec(x)"or i=="SEC"):

                                y_sec=1/np.cos(n)
                                fig,ax=plt.subplots()
                                ax.plot(n,y_sec,label='sec(x)',color='green',linewidth=2)
                                st.pyplot(fig)
                    #break
            
                            elif(i=="log" or i=="LOG"):
                

                                y=np.log(s)
                                fig,ax=plt.subplots()
                                ax.plot(s,y,label='log(x)',color='orange')
                                st.pyplot(fig)

                    #break
                            elif(i=="e^x"):
                                y_exp=np.exp(t)
                                fig,ax=plt.subplots()
                                ax.plot(t,y_exp,label='exponential',color='orange')
                                ax.title('exponential')
                                ax.xlabel('x')
                                ax.ylabel('exponential')
                                st.pyplot(fig)
                    
                            else:
                                flag=1
                if(flag==1):
                        print("no more function found")




      


    
    
    








