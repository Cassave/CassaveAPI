def get_label(label):

    diseases = [
        {
            "label": "0",
            "title": "Bacteriosis Vascular",
            "description": "Enfermedad causada por la bacteria Xanthomonas axonopodis pv. manihotis. Desarrolla manchas angulares en las hojas y añublo, marchitamiento, entre otros. En el peor de los casos, si no se toman las medidas adecuadas para su control, puede generar pérdidas de hasta un 100% de la producción.",
            "symptoms": "Este patógeno desarrolla manchas angulares en las hojas, añublo (aspecto de quemazón), marchitamiento, secreción de sustancias en el tallo. Las manchas que aparecen en las hojas exudan una sustancia amarillenta y pegajosa, concentrada en gotas.",
            "vectors": "La sustancia exudada por las plantas afectadas puede esparcirse a otras plantas, a través de las gotas y salpicaduras de agua producto de la lluvia. Además, los insectos pueden esparcir esta sustancia a plantas sanas, sin embargo es poco común. El uso de esquejes infectados puede transmitir esta bacteria a nuevos cultivos.",
            "treatment": "No existe un tratamiento que elimine directamente al virus, sin embargo, se puede evitar realizando ciertas prácticas. Es de importancia sepultar o incinerar las plantas afectadas, esto garantiza que no se infecten nuevas zonas o cultivos. Además, se debe buscar tener material de siembra limpio, esto es esencial para mantener la enfermedad en niveles bajos.",
            "recommendation": [
                "Usar esquejes sanos y de variedades resistentes.",
                "No usar herramientas agrícolas, antes usadas en cultivos afectados, en los cultivos sanos, a menos que se haga una correcta limpieza y desinfección de los mismos.",
                "Tener cuidado en la manipulación de heridas en plantas sanas, ya que se puede transmitir la bacteria a través de estas heridas."
            ]
        },
        {
            "label": "1",
            "title": "Raya Parda",
            "description": "Causada por el agente Cercosporidium Henningsii, desarrolla manchas foliares y genera una tonalidad amarilla en las hojas de la planta, hasta que finalmente se secan y caen a razón de las sustancias tóxicas secretadas por el patógeno.",
            "symptoms": "Desarrollo de clorosis o aparición de manchas de color amarillo o verde claro en las hojas de la planta de Yuca. Aquellas plantas afectadas presentarán una reducción considerable de su tamaño y el del tubérculo. Estos síntomas serán más severos en climas fríos, pues es más favorable para el virus.",
            "vectors": "El viento y la lluvia pueden transportar partes de las lesiones de tejidos de las plantas infectadas, a zonas y plantas sanas.",
            "treatment": "Si bien no existe un tratamiento químico para ello, se recomienda evitar aquellas prácticas agronómicas que aumenten la humedad en la zona de plantación. Además, el uso de fungicidas a base de óxido de cobre y oxicloruro de cobre puede hacer frente a este hongo.",
            "recommendation": [
                "Usar esquejes no infectados para nuevos cultivos.",
                "Aplicar prácticas agronómicas que reduzcan el exceso de humedad en la plantación.",
                "Usar herramientas agrícolas desinfectadas."
            ]
        },
        {
            "label": "2",
            "title": "Ácaro Verde",
            "description": "También conocido como Mononychellus Tanajoa, es una plaga que se alimentan del envés de las hojas más jóvenes de la planta de yuca, desarrollando un aspecto moteado, bronceado y con puntos cloróticos. Puede reducir entre un 21% y 73% del rendimiento de producción.",
            "symptoms": "El ácaro verde se alimenta del envés de las hojas más jóvenes de la yuca, ocasionando que estas desarrollen una apariencia moteada, con una tonalidad bronceada, con puntos cloróticos y una reducción considerable de tamaño.",
            "vectors": "Las afectaciones son generadas por el ácaro verde Mononychellus Tanajoa, que se alimenta del envés o cogollos de plantas jóvenes de la yuca.",
            "treatment": "No existe un tratamiento químico recomendable para el control de esta plaga, pues puede desarrollar resistencias en otras enfermedades desarrollables en los cultivos de yuca.",
            "recommendation": [
                "Usar esquejes o material de siembra sano, y de variedades resistentes o tolerantes a la plaga.",
                "Uso de plaguicidas selectivos, y que protejan la población de enemigos naturales.",
                "Realizar un monitoreo a la zona de cultivo, para detectar posibles poblaciones de la plaga, más en épocas de sequía."
            ]
        },
        {
            "label": "3",
            "title": "Mosaico Común",
            "description": "Enfermedad causada por el virus CsCMV, del grupo de los Potexvirus. Desarrollan síntomas de mosaico y clorosis (manchas amarillas en la hoja). La presencia de este virus puede significar un crecimiento reducido de la planta y del tubérculo.",
            "symptoms": "Desarrollo de clorosis o aparición de manchas de color amarillo o verde claro en las hojas de la planta de Yuca. Aquellas plantas afectadas presentarán una reducción considerable de su tamaño y el del tubérculo. Estos síntomas serán más severos en climas fríos, pues es más favorable para el virus.",
            "vectors": "Se propaga fácilmente al usar material vegetal infectado. Del mismo modo, su estabilidad le permite ser transmitido a través de implementos usados en labores agrícolas. Otra vector de transmisión es la mosca blanca.",
            "treatment": "No existe un tratamiento que elimine directamente al virus, sin embargo, se puede evitar a partir de la higiene de los implementos de labores agrícolas, el uso de esquejes no infectados y ejecución de tratamientos biológicos para el manejo de vectores de transmisión biológicos.",
            "recommendation": [
                "Usar esquejes sanos, en terrenos sanos.",
                "Identificar aquellas plantas afectadas por este virus, y eliminarlas, quemarlas es una buena opción.",
                "Evitar cultivar en terrenos vecinos a áreas infectados."
            ]
        },
        {
            "label": "4",
            "title": "Planta Sana",
            "description": "La planta es saludable. Mantener un monitoreo periódico te permitirá identificar plagas y enfermedades a tiempo."
        }
    ]
    return diseases[label]
