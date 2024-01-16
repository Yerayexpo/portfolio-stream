import streamlit as st
from streamlit.components.v1 import components
from PIL import Image

st.set_page_config(page_title='Yeray Exposito', 
                   page_icon='✌️', 
                   layout="centered",
)

st.markdown("<h1 style='text-align: center; color: #af2222;'>Portfolio de un Data Scientist 🔎</h1>", unsafe_allow_html=True)

index = 0
enlace_linkedin = '<a href="https://linkedin.com/in/yeray-exposito"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png" width="40" height="40"></a>'
enlace_github = '<a href="https://github.com/Yerayexpo"><img src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" width="40" height="40"></a>'
enlace_curriculum = '<a href="https://drive.google.com/file/d/1AQHQJETWni3HffHvvci3BAJNsXGkeM-7/view?usp=drive_link"><img src="https://cdn-icons-png.flaticon.com/512/3789/3789854.png" width="40" height="40"></a>'
enlaces_unidos = enlace_linkedin + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + enlace_github + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + enlace_curriculum

st.markdown("""
        <style>
            body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
          .circle-image {
              width: 200px;
              height: 200px;
              border-radius: 50%;
              overflow: hidden;
              box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
              border: 2px solid #af2222;
          }
          
          .circle-image img {
              width: 100%;
              height: 100%;
              object-fit: cover;
          }
        </style>
        """, unsafe_allow_html=True)


with st.sidebar:
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        texto = [
            "Yeray Expósito",
            "Junior Data Scientist",
            "Contacta 👇"
        ]
        st.markdown(f"""<div class="circle-image">
        <img src="https://media.licdn.com/dms/image/D4D03AQE_BiflBzJHsg/profile-displayphoto-shrink_200_200/0/1682542245244?e=1710979200&v=beta&t=ogKi8jZD1SIuxL0e3aAKi0ylo85JlWHkkbYTNaiQENM" alt="Yo">
        </div>            
        <div style='text-align: center;'>
                <h1>{texto[0]}</h1>
                <p>{texto[1]}</p>
                <p>{texto[2]}</p>
        </div>
        <div style='text-align: center;'>{enlaces_unidos}</div><br>""",unsafe_allow_html=True)
    option = st.selectbox(
        'Selecciona página',
        ('🏠 Home','👀 Análisis', '📟 Dashboards', '📔 Proyectos','🎓 Certificados/Skills'),index=0)

if option == '🏠 Home':
    st.image("https://cdn.leonardo.ai/users/d293df0e-cdbb-4d97-b51d-09f318b25c99/generations/64e63425-c6db-488b-9325-f874d6845b53/Leonardo_Diffusion_XL_I_want_a_background_of_a_data_Science_3.jpg")
    st.write("""
           ¡Hola! Bienvenido a mi Portfolio. Soy Junior Data Scientist apasionado por aprender nuevas tecnologías y progresar en el ámbito laboral. Actualmente, 
             tengo la oportunidad de trabajar como Teacher Assistant en The Bridge Digital Talent Accelerator, una experiencia que me ha enriquecido y 
             me mantiene al tanto de las últimas novedades tecnológicas.

            En esta página, encontrarás una variedad de proyectos relacionados con machine learning, que incluyen modelos, 
             visualizaciones y procesamiento de datos. Además, he desarrollado dashboards informativos para diferentes aplicaciones y proyectos, 
             así como implementaciones con Streamlit que ofrecen diversas funcionalidades.

            Te invito a explorar mi trabajo y descubrir las habilidades y conocimientos que he adquirido a lo largo de mi carrera. 
             ¡Espero que encuentres inspiración en mis proyectos y que podamos aprender juntos en este emocionante viaje hacia el mundo del Data Science!
    """)

elif option == '👀 Análisis':
    st.markdown("<h3 style='text-align: center;'>Analisis 👀 </h1>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3)
    with col1.expander('Board Games'):
        st.image("https://cdn.leonardo.ai/users/d293df0e-cdbb-4d97-b51d-09f318b25c99/generations/c792afa7-cb65-49b8-a964-11c2893e7ec6/Leonardo_Diffusion_XL_I_want_a_background_of_a_boardgame_1.jpg")
        st.markdown("""<div style='text-align: center;'><a href="https://github.com/Yerayexpo/BoardGame-Analysis" align=>Ir al Repositorio</a></div><br>""",unsafe_allow_html=True)
        st.write("""En este análisis el objetivo fue practicar la obtención, transformación y visualización de los datos para entrenar un modelo predictivo sobre la popularidad 
                 de los juegos.
                 """)
    with col2.expander('Shishas'):
        st.image("https://cdn.leonardo.ai/users/d293df0e-cdbb-4d97-b51d-09f318b25c99/generations/2b2ae344-ede7-4b2f-be4c-9e589e57f12e/Leonardo_Diffusion_XL_Backgroun_of_a_shisha_data_analysis_1.jpg")
        st.markdown("""<div style='text-align: center;'><a href="https://github.com/Yerayexpo/Shishas align=>Ir al Repositorio</a></div><br>""",unsafe_allow_html=True)
        st.write("""La empresa estaba interesada en conseguir un modelo de recomendaciones de tabacos para usuarios. 
                 Tras el análisis pudimos detectar las claves más importantes y afinar el modelo.
                 (Work in Progress) """)
    with col3.expander('Heart Disease'):
        st.image("https://cdn.leonardo.ai/users/d293df0e-cdbb-4d97-b51d-09f318b25c99/generations/01b70ab3-47d0-4782-b7e7-cadcb6844ca8/Leonardo_Diffusion_XL_I_want_a_background_of_a_heart_disease_a_0.jpg")
        st.markdown("""<div style='text-align: center;'><a href="https://github.com/Yerayexpo/Heart-Disease" align=>Ir al Repositorio</a></div><br>""",unsafe_allow_html=True)
        st.write("""Análisis docente centrado en la predicción de personas con probabilidades más elevadas de sufrir un ataque al corazón.
                """)
elif option == '📟 Dashboards':
    st.markdown("<h3 style='text-align: center;'>Dashboards 📟 </h1>", unsafe_allow_html=True)
   
    with st.expander('Students App'):

        imagenes = ['img/app/app_home.png','img/app/app_main.png','img/app/app_alumnos.png','img/app/app_eventos.png']
        imagen_actual = st.image([])

        col1, col2, col3, col4 = st.columns(4)
        if col1.button('Home'):
            index = 0
        col1.write('')
        if col2.button('Main'):
            index = 1
        col2.write('')
        if col3.button('Alumnos'):
            index = 2
        col3.write('')
        if col4.button('Eventos'):
            index = 3
        col4.write('')
        st.write(f"""Con este dahsboard podemos ver toda la información de los eventos y los alumnos de nuestra app.
                 
- Main: Usuarios activos a tiempo real, cantidad de alumnos por curso y evento más próximo.
- Alumnos: Filtrado de alumnos con todos los datos de cada uno de ellos, idioma, intereses...
- Eventos: Mapa con ubicación fecha y cantidad de alumnos que están apuntados al evento.
                """)
        imagen_path = imagenes[index]
        imagen = Image.open(imagen_path)
        imagen_actual.image(imagen, use_column_width=True)

    with st.expander('Board Games'):
        st.image("img/dash_games.png")
        st.write("""Dashboard informativo sobre los juegos más populares y mejor valorados por la plataforma BoardGameGeek, dispone de:
                 
- Filtro para poder ver las caraterísticas de los juegos más en profundidad.
- Ranking top de 5 juegos mejor valorados en la selección actual.
- Cantidad de juegos, usuarios en posesión del juego y votos.    
                 """)

    # with st.expander('otro'):
    #     st.write("""En este análisis el objetivo fue practicar la obtención, transformación y visualización de los datos.
                 
    #              """)

elif option == '📔 Proyectos':
    st.markdown("<h3 style='text-align: center;'>Proyectos 📔</h1>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3)
    with col1.expander('Apis'):
        st.image("https://cdn.leonardo.ai/users/d293df0e-cdbb-4d97-b51d-09f318b25c99/generations/73eb85b5-c7f8-4328-93e6-ae9caf79f730/Leonardo_Diffusion_XL_I_want_a_background_of_a_webcam_that_rec_0.jpg")
        st.markdown("""<div style='text-align: center;'><a href="https://desafio-api.onrender.com/" align=>Ver página</a></div><br>""",unsafe_allow_html=True)
        st.write("""Flask con 3 endpoints diferentes, un modelo generativo de imágenes, otro analizador de leguaje malsonante y un geolocalizador conectado a google maps para establecer rutas.
                 """)
    with col2.expander('Amazon Webscraping'):
        st.image("https://cdn.leonardo.ai/users/d293df0e-cdbb-4d97-b51d-09f318b25c99/generations/d5e618f3-3856-4385-bd7f-f1d6c80ddb4c/Leonardo_Diffusion_XL_I_want_a_background_of_a_webscrappgin_ap_0.jpg")
        st.markdown("""<div style='text-align: center;'><a href="https://amazon-scrapp.streamlit.app/" align=>Ver página</a></div><br>""",unsafe_allow_html=True)
        st.write("""Obtención de datos de Amazon con buscador y filtro de precio.
                 
                 """)
    with col3.expander('Sherlock'):
        st.image("https://cdn.leonardo.ai/users/d293df0e-cdbb-4d97-b51d-09f318b25c99/generations/2182e25d-ed10-4993-8e3a-b6fb6224c05c/Leonardo_Diffusion_XL_A_chaotic_and_cluttered_office_filled_wi_0.jpg")
        st.markdown("""<div style='text-align: center;'><a href="https://sherlock.streamlit.app/" align=>Ver página</a></div><br>""",unsafe_allow_html=True)
        st.write("""Página para buscar usuarios por nickname/username que devuelve una lista de todos los sitios coincidentes.
                 """)

elif option == '🎓 Certificados/Skills':
    st.markdown(
            """
        <style>
        button {
        border-radius: 50%;
        height: 3em;
        width: 3em;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )

    col1,col2,col3 = st.columns([3,1,2])
    with col1:
        st.markdown("<h3 style='text-align: center;'>Skills ⚒️</h1>", unsafe_allow_html=True)

        skills = ['Python','Pandas','Matplotlib','Git','PowerBI',
                'ML','Tensorflow','Keras','Spark','AWS',
                'Postgress','Mongodb','BFSoup','Flask','Postman']
        columns1 = st.columns(3)
        for c in range(3):
            columns1[c].button(skills[c],use_container_width=True)
        columns2 = st.columns(3)
        for c in range(3):
            columns2[c].button(skills[c+3],use_container_width=True)
        columns3 = st.columns(3)
        for c in range(3):
            columns3[c].button(skills[c+6],use_container_width=True)
        columns3 = st.columns(3)
        for c in range(3):
            columns3[c].button(skills[c+9],use_container_width=True)
        columns3 = st.columns(3)
        for c in range(3):
            columns3[c].button(skills[c+12],use_container_width=True)
    with col3:
        st.markdown("<h3 style='text-align: center;'>Certificados 📖</h1>", unsafe_allow_html=True)
        st.markdown("""
                ##### Data Science
- [Bootcamp Data Science](https://www.linkedin.com/in/yeray-exposito/details/certifications/1635549068705/single-media-viewer/?profileId=ACoAADuEGKEBItzwcB_80ChXwCjCCFIAgvWeQBc)
                
 ##### AWS
- [Fundamentals](https://coursera.org/share/6e4b6bd071c8d62c7bbe1d41c67fa71f)
- [Cloud Technical Essentials](https://coursera.org/share/215bc7f370749f52a47ba733c5a509da)
- [Migratin to the AWS Cloud](https://coursera.org/share/ced424a57dc447b5dfdafc5fad6f08bf)
- [Architecting Solutions](https://coursera.org/share/58c212befcdeaaa3c25466a1a92f5f91)

                
##### Linkedin
- [Generative AI](https://www.linkedin.com/learning/certificates/08ad4b17afced537f3edd45e452800fa150b57333639a9738ea6cde03592aa10)
- [Streaming yoru work with Bing Chat](https://www.linkedin.com/learning/certificates/38bfd4b7adc042b076dce46086827d64af6f73360a42181d456e8983b75521ea)
- [Microsoft 365 Copilot](https://www.linkedin.com/learning/certificates/41553c09c55a5253ac11dd09a0900656d67cda7e33c9dcabc499445d331ce873)
                
##### Microsoft
- [Career Essentials in Generative AI](https://www.linkedin.com/learning/certificates/bc684d8b427e78bb78b7b38e88e92c07598b509bd666b103b00afbf813776fe9)

""")


