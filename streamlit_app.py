import streamlit as st

import shutil
import pyvista as pv
from stpyvista import stpyvista
import os

from PIL import Image

import cadquery as cq


#@st.cache_resource
st.set_page_config(
    page_title="Nexymake 0.0.1",
    page_icon="img/gorila.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def main():
    st.title("It's winter!")
    st.markdown(
        "hola Mundo..."
    )
    
    word = st.text_input("Ingrese una palabra:")
    in_stl =st.text_input("Nombre STL")
    placeholder=st.empty()
    if word: 
        texto=cq.Workplane().text(word, 5, 1, fontPath="fonts/vinet.ttf") #fontPath
        #texto=cq.Workplane().text(palabra, 5, 1, font='Arial')
        stl_done=texto.val()
        name_stl=in_stl+".stl"
        st.write("creado con cq")
        # Obtener la ruta del directorio del archivo ejecutable
        if in_stl:
            stl_done.exportStl(name_stl)
            current_directory = os.path.dirname(__file__)
            # Construir la ruta completa para el archivo STL
            stl_file_path = os.path.join(current_directory, name_stl)
            st.write(stl_file_path)

            if st.button("Ver STL"):
                plotter = pv.Plotter(window_size=[400, 300])
                # Load the STL files and add the vectors to the plot
                mesh = pv.read(stl_file_path)
                plotter.add_mesh(mesh,show_edges=False, color="blue")
                plotter.background_color="white"
                #plotter.add_text("3D",font_size=5)
                plotter.view_isometric()
                # Show the plot to the screen
                with placeholder.container():
                    stpyvista(plotter)
                    plotter.show()

    
    # c1, c2 = st.columns(2)

    # c1.image(
    #     Image.open("img/aphex.png"), 
    #     use_column_width="always"
    # )
    # c2.image(
    #     Image.open("img/robot.png"), 
    #     use_column_width="always"
    # )r
    
    
    # Seleccionar un archivo STL
    #st.sidebar.title("Seleccionar Archivo")
    #upload_file = st.sidebar.file_uploader("Cargar archivo STL", type="stl")
    #if upload_file is not None:
    # if st.button('Ver STL'):
    #     plotter = pv.Plotter(window_size=[300,300])
    #     # Load the STL files and add the vectors to the plot
    #     mesh = pv.read("ca.stl")
    #     plotter.add_mesh(mesh,show_edges=False, color="blue")
    #     plotter.background_color="white"
    #     plotter.view_isometric()

    #     # Show the plot to the screen
    #     stpyvista(plotter)
             # Seleccionar un archivo STL
    st.sidebar.title("Seleccionar Archivo")
    upload_file = st.sidebar.file_uploader("Cargar archivo STL", type="stl")
    
    if upload_file is not None:
        # save the uploaded file to disk
        with open("stlfile.stl", "wb") as buffer:
            shutil.copyfileobj(upload_file, buffer)

        plotter = pv.Plotter(window_size=[300,300])

        # Load the STL files and add the vectors to the plot
        mesh = pv.read("stlfile.stl")
        plotter.add_mesh(mesh,show_edges=False, color="blue")
        plotter.background_color="white"
        plotter.view_isometric()

        # Show the plot to the screen
        stpyvista(plotter)


if __name__ == "__main__":
    main()
