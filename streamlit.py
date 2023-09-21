import folium
import streamlit as st
from streamlit_folium import st_folium

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

    equipos_huawei = [
        {"nombre": "OLT Huawei 5608T", "descripcion": "Equipo central de la red GPON que controla la distribución de datos a través de la fibra óptica hacia las ONUs en las sedes remotas.", "datasheet": "https://domusntw.com/wp-content/uploads/HUAWEI-OLT-MA5608T_Datasheet.pdf", "imagen": "HuaweiMA5608T.png", "precio": 5000},
        {"nombre": "Splitter Huawei 1x32", "descripcion": "Splitter óptico utilizado para dividir la señal óptica hacia múltiples ONUs en cada sede.", "datasheet": "http://www.keweifiber.com/1x4-1x8-1x16-1x32-1x64-compact-splitter-1-8-port-FDT-Huawei-Optical-Fiber-PLC-Splitter-LGX-type-Splitter-Planar-Light-Circuit-pd44474841.html", "imagen": "Huaweisplitter.jpg", "precio": 200},
        {"nombre": "ONU Huawei EG8010H", "descripcion": "Unidades de red en las sedes remotas que brindan servicios de banda ancha GPON a los usuarios.", "datasheet": "https://www.router-switch.com/huawei-eg8010h-datasheet-pdf.html", "imagen": "huaweiEG8010H.jpg", "precio": 1000},
        {"nombre": "Splitter Huawei 1x8", "descripcion": "Splitter óptico utilizado en el trayecto a Piedecuesta para dividir la señal óptica hacia múltiples ONUs.","datasheet": "http://www.keweifiber.com/1x4-1x8-1x16-1x32-1x64-compact-splitter-1-8-port-FDT-Huawei-Optical-Fiber-PLC-Splitter-LGX-type-Splitter-Planar-Light-Circuit-pd44474841.html" ,"imagen": "Huaweisplitter.jpg", "precio": 1000},
        {"nombre": "Cisco ONS 15454 MSTP 1", "descripcion": "Amplificador óptico (repetidor óptico) utilizado en el trayecto a Bucaramanga para mantener la calidad de la señal óptica.", "datasheet": "https://www.cisco.com/c/en/us/products/collateral/optical-networking/ons-15454-m6-multiservice-transport-platform-mstp/data_sheet_c78-601956.html", "imagen": "CISCOONS15454.jpg", "precio": 300},
        {"nombre": "Splitter Huawei 1x4", "descripcion": "Splitter óptico utilizado en el trayecto a Bucaramanga para dividir la señal óptica hacia múltiples ONUs.","datasheet": "http://www.keweifiber.com/1x4-1x8-1x16-1x32-1x64-compact-splitter-1-8-port-FDT-Huawei-Optical-Fiber-PLC-Splitter-LGX-type-Splitter-Planar-Light-Circuit-pd44474841.html", "imagen": "Huaweisplitter.jpg", "precio": 1000},
        {"nombre": "Cisco ONS 15454 MSTP 2", "descripcion": "Amplificador óptico (repetidor óptico) utilizado en el trayecto a Bucaramanga para mantener la calidad de la señal óptica.", "datasheet": "https://www.cisco.com/c/en/us/products/collateral/optical-networking/ons-15454-m6-multiservice-transport-platform-mstp/data_sheet_c78-601956.html", "imagen": "CISCOONS15454.jpg", "precio": 300},
        {"nombre": "Splitter Huawei 1x2", "descripcion": "Splitter óptico utilizado en el trayecto a El Limonal para dividir la señal óptica hacia múltiples ONUs.","datasheet": "http://www.keweifiber.com/1x4-1x8-1x16-1x32-1x64-compact-splitter-1-8-port-FDT-Huawei-Optical-Fiber-PLC-Splitter-LGX-type-Splitter-Planar-Light-Circuit-pd44474841.html", "imagen": "Huaweisplitter.jpg", "precio": 1000},
        {"nombre": "Cisco ONS 15454 MSTP 3", "descripcion": "Amplificador óptico (repetidor óptico) utilizado en el trayecto a El Limonal para mantener la calidad de la señal óptica.","datasheet": "https://www.cisco.com/c/en/us/products/collateral/optical-networking/ons-15454-m6-multiservice-transport-platform-mstp/data_sheet_c78-601956.html" ,"imagen": "CISCOONS15454.jpg", "precio": 300},
    ]

    # Calcular el costo total del presupuesto
    costo_total = sum(equipo['precio'] for equipo in equipos_huawei)

    st.subheader("Equipos Huawei GPON")
    st.write("Presupuesto Total: $", costo_total)

    # Mostrar los datos de los equipos
    for equipo in equipos_huawei:
        st.write(f"**{equipo['nombre']}**")
        st.write(f"Descripción: {equipo['descripcion']}")
        st.write(f"Precio: ${equipo['precio']}")
        st.markdown(f"[Enlace al datasheet]({equipo['datasheet']})")
        st.image(equipo['imagen'], use_column_width=True)

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

    # Llama a la función st_folium para renderizar el mapa de Folium en Streamlit
    st_data = st_folium(m, width=725)

if __name__ == "__main__":
    main()