import folium
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd

def main():
    st.title("Red Óptica Pasiva Gigabit (GPON) - Conexión entre Sedes")

    st.write("""
    Una Red Óptica Pasiva Gigabit (GPON) es una tecnología de red de fibra óptica de alta velocidad utilizada para proporcionar servicios de banda ancha, como Internet de alta velocidad, televisión y telefonía, a los usuarios finales. A continuación, se presentan algunas de las características clave de una Red GPON:

    1. *Alta Velocidad*: Una GPON ofrece velocidades de transmisión de datos de hasta varios gigabits por segundo, lo que la hace adecuada para aplicaciones que requieren un ancho de banda significativo.

    2. *Compartición de Fibra Óptica*: Al igual que con las PON, en una GPON, múltiples usuarios comparten una única fibra óptica para la transmisión y recepción de datos. Esto permite un uso eficiente de la infraestructura de fibra.

    3. *Distribución Punto a Multipunto*: La topología de una GPON es punto a multipunto, lo que significa que un único equipo en el extremo de la red (OLT) se conecta a múltiples equipos en el extremo del usuario (ONU). Esto permite que múltiples usuarios se conecten a través de una sola fibra.

    4. *Triple Play*: Las GPON son ideales para ofrecer servicios "Triple Play", que incluyen Internet de alta velocidad, televisión y telefonía a través de una sola conexión de fibra óptica.

    5. *Mayor Alcance*: Las GPON tienen un mayor alcance en comparación con las PON tradicionales, lo que significa que pueden servir a usuarios que se encuentran a distancias más largas del punto de acceso.

    6. *Seguridad*: La tecnología GPON ofrece características de seguridad avanzadas, como cifrado de datos, que protegen la privacidad de los usuarios.

    7. *Escalabilidad*: Las GPON son escalables y pueden acomodar un número creciente de usuarios agregando más ONUs en el extremo del usuario.

    En resumen, una Red Óptica Pasiva Gigabit (GPON) es una solución de alta velocidad y eficiente en términos de ancho de banda para proporcionar una amplia gama de servicios a los usuarios finales utilizando tecnología de fibra óptica y una arquitectura de red pasiva.
    """)

        
    tab1, tab2, tab3, tab4 = st.tabs(["OLT Huawei 5608T", "Splitter Huawei", "ONU Huawei EG8010H", "Cisco ONS 15454 MSTP"])

    with tab1:
        
       st.header("OLT Huawei 5608T")
       
    
       imagen_url1 = "https://sc01.alicdn.com/kf/H7dcfbee642ae477da308158e4478831fu.png" 
       st.image(imagen_url1, caption=' Huawei MA5608T-24', use_column_width=True)
       st.write(" Equipo central de la red GPON que controla la distribución de datos a través de la fibra óptica hacia las ONUs en las sedes remotas.")
       st.subheader("Información sobre el MA5608T-24 (CARACTERISTICAS)")
       texto_largo1 = """
       - **24 puertos:** Como su nombre indica, esta OLT tiene 24 puertos, lo que significa que puede servir hasta 24 clientes u ubicaciones finales en la red GPON.
    
       - **Capacidad de Escalabilidad:** Aunque tiene un número limitado de puertos, el MA5608T-24 es escalable y puede expandirse con el tiempo para agregar más puertos o capacidades a medida que crece la red.
    
       - **Interfaces de Conexión:** Proporciona interfaces para conexiones GPON y Ethernet para conectar clientes y otros dispositivos en la red.
    
       - **Gestión Avanzada:** Ofrece herramientas avanzadas de gestión y administración para facilitar la configuración, supervisión y mantenimiento de la red.
    
       - **Compatibilidad con Servicios de Banda Ancha:** Puede ofrecer servicios de banda ancha de alta velocidad, incluyendo Internet, voz y video a los clientes conectados.
    
       - **Alta Disponibilidad:** Está diseñado para proporcionar alta disponibilidad y confiabilidad en la red.
    
    
       """
    
    
    
       st.markdown(texto_largo1)
       datasheet1 = 'https://domusntw.com/wp-content/uploads/HUAWEI-OLT-MA5608T_Datasheet.pdf'
       
       st.subheader("Datasheet y Caracteristicas")
       
       if st.button('Ir a la Página 1'):
           
           st.markdown(f'[Huawei MA5608T-24]({datasheet1})')
    
       
       
    
    with tab2:
        
       st.header("Splitter Huawei")
       imagen_url2 = "https://es.springoptical.com/Content/File_Img/S_Product/2016-08-09/201608091628277492918.jpg" 
       st.image(imagen_url2, caption='Splitter Huawei', use_column_width=True)
       st.write("Splitter óptico utilizado para dividir la señal óptica hacia múltiples ONUs en cada sede.")
       st.subheader("Información sobre el Splitter Huawei (CARACTERISTICAS)")
       texto_largo2 = """
       - **El Huawei splitter es un dispositivo pasivo que divide una señal de fibra óptica en dos o más señales.

       - **El Huawei splitter está disponible en varios modelos, con diferentes rangos de división y pérdidas de inserción.

       - **El rango de división indica el número de señales en las que se dividirá la señal original.

       - **La pérdida de inserción indica la cantidad de potencia que se pierde al dividir la señal.

       - **Cuanto menor sea la pérdida de inserción, mejor será la calidad de la señal.
       
    
       """
       
       st.markdown(texto_largo2)
       
       datasheet2 = 'http://www.keweifiber.com/1x4-1x8-1x16-1x32-1x64-compact-splitter-1-8-port-FDT-Huawei-Optical-Fiber-PLC-Splitter-LGX-type-Splitter-Planar-Light-Circuit-pd44474841.html'
       
       st.subheader("Datasheet y Caracteristicas")
       
       if st.button('Ir a la Página 2'):
           
           st.markdown(f'[Splitter Huawei]({datasheet2})')
       
       
    
    with tab3:
        
       st.header("ONU Huawei EG8010H")
       imagen_url3 = "https://www.batna24.com/products/DNXFLPQLGRMMPL/hg8310m/8310m.webp" 
       st.image(imagen_url3, caption='ONU Huawei EG8010H', use_column_width=True)
       st.write("Unidades de red en las sedes remotas que brindan servicios de banda ancha GPON a los usuarios.")
       st.subheader("Información sobre el ONU Huawei EG8010H (CARACTERISTICAS)")
       
       texto_largo3 = """
       - **El Huawei EG8010H es un terminal de red óptica (ONT) para interiores utilizado en la solución FTTH de Huawei.
       
       - **El EG8010H proporciona acceso por banda ultraancha a usuarios domésticos y pequeñas oficinas mediante el uso de la tecnología GPON.
       
       - **El EG8010H tiene un puerto PON GPON y un puerto Ethernet GE.
       
       - **El EG8010H soporta velocidades de datos de hasta 2,5 Gbps de descarga y 1,25 Gbps de subida.
       
       - **El EG8010H soporta IPv4 e IPv6.
       
       - **El EG8010H soporta VLAN, QoS y ACL.
       
       - **El EG8010H soporta enrutamiento NAT y DHCP.
       
       - **El EG8010H soporta bridge mode y routing mode.
       
       - ** El EG8010H soporta TR-069 para gestión remota.
       
       
       """
       
       st.markdown(texto_largo3)
       
       datasheet3 = 'https://www.router-switch.com/huawei-eg8010h-datasheet-pdf.html", "imagen": "huaweiEG8010H.jpg'
       
       st.subheader("Datasheet y Caracteristicas")
       
       if st.button('Ir a la Página 3'):
           
           st.markdown(f'[ONU Huawei EG8010H]({datasheet3})')
    
    with tab4:
        st.header("Cisco ONS 15454 MSTP")
        imagen_url4 = "https://live.staticflickr.com/6052/6377796155_87d1b86f4c_b.jpg" 
        st.image(imagen_url4, caption='Cisco ONS 15454 MSTP', use_column_width=True)
        st.write("Amplificador óptico (repetidor óptico) utilizado en el trayecto a El Limonal para mantener la calidad de la señal óptica.")
        st.subheader("Información sobre Cisco ONS 15454 MSTP (CARACTERISTICAS)")
        
        texto_largo4 = """
        - **El Cisco ONS 15454 MSTP es una plataforma de transporte multiservicio que proporciona capacidad, inteligencia e interoperabilidad para redes ópticas de próxima generación.

        - **El ONS 15454 MSTP está disponible en varios modelos, con diferentes capacidades y características.

        - **El ONS 15454 MSTP puede transportar una amplia gama de servicios, incluyendo voz, datos, video y servicios de misión crítica.

        - **El ONS 15454 MSTP es compatible con los estándares de la industria, lo que facilita su integración con otras redes.
        
        """
        
        st.markdown(texto_largo4)
        
        datasheet4 = 'https://www.cisco.com/c/en/us/products/collateral/optical-networking/ons-15454-m6-multiservice-transport-platform-mstp/data_sheet_c78-601956.html'
        
        st.subheader("Datasheet y Caracteristicas")
        
        if st.button('Ir a la Página 5'):
            
            st.markdown(f'[Cisco ONS 15454 MSTP-E]({datasheet4})')    
            
    data = pd.DataFrame({
    "Equipo": ["OLT", "Splitter", "ONU", "ONS", "TOTAL"],
    "Marca": ["Huawei", "Huawei", "Huawei", "Cisco", "-"],
    "Modelo": ["MA5608T-24", "GENERICO", "EG8010H", "15454 MSTP","-"],
    "Cantidad": ["1", "4", "1", "3","9"],
    

    "Precio x Unid": ["US$ 970.00", "US$ 30.00", "US$ 7.50","US$ 1415.00", "US$ 2422.50"], 
    "Precio Total": ["US$ 970.00 ", "US$ 120.00", "US$ 7.50","US$ 4245.00", "US$ 5342.50"]
    })

# Título de la página


# Crear una tabla en Streamlit para mostrar y editar los datos
    table = st.table(data)        

    # Ubicaciones de las sedes de la Universidad Santo Tomás
    ubicaciones_sedes = {
        "Sede Bucaramanga": {"lat": 7.136816, "lon": -73.128325},
        "Sede Floridablanca": {"lat": 7.065711, "lon": -73.095196},
        "Sede Piedecuesta": {"lat": 7.022890, "lon": -73.059422},
        "Sede El Limonal": {"lat": 7.007950, "lon": -73.051385},
    }

    # Ubicaciones de los equipos
    ubicaciones_equipos = {
        "OLT Huawei 5608T": {"lat": 7.136900, "lon": -73.128300},  # En Sede Bucaramanga
        "Splitter Huawei 1x32": {"lat": 7.065750, "lon": -73.095200},  # En Sede Floridablanca
        "ONU Huawei EG8010H": {"lat": 7.022950, "lon": -73.059420},  # En Sede Piedecuesta
        "Splitter Huawei 1x8": {"lat": 7.007950, "lon": -73.051385},  # En Sede El Limonal
        "Cisco ONS 15454 MSTP 1": {"lat": 7.099925989275754, "lon": -73.11067795083181},  # Entre Sede Bucaramanga y Floridablanca
        "Splitter Huawei 1x4": {"lat": 7.040196322502624, "lon": -73.07383803488932},  # Entre Sede Floridablanca y Piedecuesta
        "Cisco ONS 15454 MSTP 2": {"lat": 7.014978071217734, "lon": -73.05534150714179},  # Entre Sede Piedecuesta y El Limonal
        "Splitter Huawei 1x2": {"lat": 7.007950, "lon": -73.051385},  # Entre Sede El Limonal y Trayecto
        "Cisco ONS 15454 MSTP 3": {"lat": 7.092093, "lon": -73.100384},  # En Trayecto
    }

    # Crear un mapa de Folium
    m = folium.Map(location=[7.092093, -73.100384], zoom_start=13)

    # Agregar marcadores para las sedes
    for sede, ubicacion in ubicaciones_sedes.items():
        folium.Marker(
            [ubicacion["lat"], ubicacion["lon"]],
            popup=sede,
            tooltip=sede,
            icon=folium.Icon(color='green')
        ).add_to(m)

    # Agregar marcadores para los equipos
    for equipo, ubicacion in ubicaciones_equipos.items():
        folium.Marker(
            [ubicacion["lat"], ubicacion["lon"]],
            popup=equipo,
            tooltip=equipo
        ).add_to(m)

    # Conectar los equipos con líneas
    sedes = list(ubicaciones_sedes.values())
    for i in range(len(sedes) - 1):
        folium.PolyLine(
            locations=[[sedes[i]["lat"], sedes[i]["lon"]], [sedes[i + 1]["lat"], sedes[i + 1]["lon"]]],
            color='blue',
            weight=2.5
        ).add_to(m)

    # Agregar líneas de conexión entre los equipos Cisco ONS en el trayecto
    cisco_ons_trayecto = [ubicaciones_equipos["Cisco ONS 15454 MSTP 1"], ubicaciones_equipos["Cisco ONS 15454 MSTP 2"], ubicaciones_equipos["Cisco ONS 15454 MSTP 3"]]
    for i in range(len(cisco_ons_trayecto) - 1):
        folium.PolyLine(
            locations=[[cisco_ons_trayecto[i]["lat"], cisco_ons_trayecto[i]["lon"]],
                       [cisco_ons_trayecto[i + 1]["lat"], cisco_ons_trayecto[i + 1]["lon"]]],
            color='red',  # Cambia el color de las líneas si lo deseas
            weight=2.5
        ).add_to(m)
        
        # Agregar hexágono para la celda de cobertura de red óptica
    folium.Circle(
        location=[7.136844296154591, -73.12832180456587],  # Ubicación de la sede Bucaramanga
        fill_color='red',
        fill_opacity=0.5,
        number_of_sides=6,  # Hexágono
        radius=50,  # Radio del hexágono en metros
        
        tooltip='Celda Cobertura Sede Bucaramanga'
    ).add_to(m)
    
    
    
    folium.Circle(
        location=[7.066195857926469, -73.09492035409652],  # Ubicación de la sede Bucaramanga
        fill_color='red',
        fill_opacity=0.5,
        number_of_sides=6,  # Hexágono
        radius=110,  # Radio del hexágono en metros
        
        tooltip='Celda Cobertura Sede Floridablanca'
    
    ).add_to(m)
    folium.Circle(
        location=[7.023262911646313, -73.05971245467781],  # Ubicación de la sede Bucaramanga
        fill_color='red',
        fill_opacity=0.5,
        number_of_sides=6,  # Hexágono
        radius=150,  # Radio del hexágono en metros
        
        tooltip='Celda Cobertura Sede Piedecuesta'
    ).add_to(m)
    folium.Circle(
        location=[7.0084293135346725, -73.05136176052113],  # Ubicación de la sede Bucaramanga
        fill_color='red',
        fill_opacity=0.5,
        number_of_sides=6,  # Hexágono
        radius=80,  # Radio del hexágono en metros
        
        tooltip='Celda Cobertura Sede Limonal'
    ).add_to(m)
        
        

    # Llama a la función st_folium para renderizar el mapa de Folium en Streamlit
    st_data = st_folium(m, width=725)

if __name__ == "__main__":
    main()
