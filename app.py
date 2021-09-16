from bs4 import BeautifulSoup
from flask_cors import cross_origin
from flask import Flask, render_template, request, send_file, Response

import pandas as pd
import requests
from urllib.request import urlopen, Request
import datetime 

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
  if request.method == 'POST':
    return "POST"
  else:
    b=""
    a=""
    for l in lista(): 	
          b+=scrap(l)



    now = datetime.datetime.now()
    sumar=datetime.timedelta(hours = -3)
    now=now+sumar
    nw=str(now.strftime("%Y-%m-%d %H-%M-%S"))
    return Response(b,mimetype="text/csv",headers={"Content-disposition": "attachment; filename="+nw+".csv"})
 


if __name__ == "__main__":
    app.run(port=8000, debug=True)


def archivo(b):
  File_object = open(r"Archivo.txt","w")
  return File_object.write(b)


def scrap(site):
    r = requests.get(site)
    b=""
    
    try:
        soup = BeautifulSoup(r.content, 'html.parser')
        b+=soup.find("span", {"class": "vtex-breadcrumb-1-x-term vtex-breadcrumb-1-x-term--breadcrumb-style ph2 c-on-base"}).text    
        b+=";"
        b+=soup.find("span", {"class": "vtex-product-price-1-x-currencyInteger vtex-product-price-1-x-currencyInteger--shelf-main-selling-price"}).text
        b+=","
        b+=soup.find("span", {"class": "vtex-product-price-1-x-currencyFraction vtex-product-price-1-x-currencyFraction--shelf-main-selling-price"}).text    
        b+="\n"
    except:
        _
    
    return b


def lista(): 
    return {"https://www.vea.com.ar/galletitas-lincoln-angry-birds/p",
"https://www.vea.com.ar/galletitas-criollitas-de-agua-x100gr/p",
"https://www.vea.com.ar/galletitas-criollitas-x400g/p",
"https://www.vea.com.ar/galletitas-media-tarde-de-agua-x-321-gr/p",
"https://www.vea.com.ar/hamburguesas-good-mark-de-carne-4-u-320-gr/p",
"https://www.vea.com.ar/hamburguesa-union-ganadera-4-u-332-gr/p",
"https://www.vea.com.ar/salchichas-paladini-tipo-viena-sin-piel-225-gr-6-u/p",
"https://www.vea.com.ar/salchichas-paty-de-viena-6-u-225-gr/p",
"https://www.vea.com.ar/salchichas-granja-iris-americana-225-gr-5-u/p",
"https://www.vea.com.ar/jamon-cocido-paladini-feteado-200-gr/p",
"https://www.vea.com.ar/jamon-cocido-campo-austral-3/p",
"https://www.vea.com.ar/salchichon-lario-2/p",
"https://www.vea.com.ar/salame-milan-lario-feteado-x-150g/p",
"https://www.vea.com.ar/aceite-cocinero-girasol-2/p",
"https://www.vea.com.ar/aceite-canuelas-de-girasol-x-900-ml/p",
"https://www.vea.com.ar/leche-entera-clasica-la-serenisima-sachet-1-l/p",
"https://www.vea.com.ar/leche-entera-3-armonia-sachet-1-l/p",
"https://www.vea.com.ar/leche-en-polvo-nido-3-prebio-1-leche-800g/p",
"https://www.vea.com.ar/queso-pategras-la-serenisima-paq-x-kg-2/p",
"https://www.vea.com.ar/queso-pategras-sancor-tradicional-ca-pintado-1-kg/p",
"https://www.vea.com.ar/yogurisimo-firme-preform-fortifizado-190-gr-frutilla/p",
"https://www.vea.com.ar/yogur-firme-la-serenisima-vainilla-190-gr/p",
"https://www.vea.com.ar/dulce-de-leche-clasico-la-serenisima-400-gr/p",
"https://www.vea.com.ar/dulce-de-leche-familiar-milkaut-x-405-gr/p",
"https://www.vea.com.ar/huevos-blancos-la-piara-x-12u-carton/p",
"https://www.vea.com.ar/huevos-blancos-la-piara-x6u-carton/p",
"https://www.vea.com.ar/tomate-perita-molto-entero-x-400-gr/p",
"https://www.vea.com.ar/arvejas-pagos-del-sur-x-350-grs/p",
"https://www.vea.com.ar/arvejas-secas-remojadas-molto-brk-gr-200/p",
"https://www.vea.com.ar/sal-fina-dos-anclas-x500gr/p",
"https://www.vea.com.ar/sal-fina-celusal-3/p",
"https://www.vea.com.ar/flan-royal-x60gr/p",
"https://www.vea.com.ar/exquisita-flan-de-vainilla-x60-gr/p",
"https://www.vea.com.ar/flan-vainill-godet-30-gr/p",
"https://www.vea.com.ar/gaseosa-coca-cola-sabor-original-2-25-l/p",
"https://www.vea.com.ar/gaseosa-cola-pepsi-regular-2-25l/p",
"https://www.vea.com.ar/agua-mineral-de-manantial-eco-de-los-andes-con-gas-1-5-l/p",
"https://www.vea.com.ar/agua-villavicencio-pet-sin-gas-1-5-l/p",
"https://www.vea.com.ar/agua-baja-en-sodio-glaciar-2-l/p",
"https://www.vea.com.ar/cerveza-brahma-chopp-rubia-1lt-retornable/p",
"https://www.vea.com.ar/cerveza-schneider-rubia-1lt/p",
"https://www.vea.com.ar/vino-de-mesa-pico-de-oro-tinto-1-l/p",
"https://www.vea.com.ar/vino-suc-abel-michel-torino-tinto/p",
"https://www.vea.com.ar/cafe-la-virginia-molido-500gr/p",
"https://www.vea.com.ar/cafe-la-planta-de-cafe-molido-260g/p",
"https://www.vea.com.ar/granby-jabon-para-ropa-polvo-baja-espuma-800-gr/p",
"https://www.vea.com.ar/detergente-en-polvo-zorro-baja-espuma/p",
"https://www.vea.com.ar/jabon-en-polvo-ala-lavado-a-mano-con-perlas-suavizantes-800-g/p",
"https://www.vea.com.ar/lavavajillas-zorro-colageno-cremo-750ml/p",
"https://www.vea.com.ar/ala-jabon-para-ropa-en-pan-multiaccion-200-gr/p",
"https://www.vea.com.ar/lavandina-ayudin/p",
"https://www.vea.com.ar/lavandina-querubin-2/p",
"https://www.vea.com.ar/shampoo-para-bebe-johnson-s-rulos-definidos-400-ml/p",
"https://www.vea.com.ar/shampoo-sedal-ceramidas-340ml/p",
"https://www.vea.com.ar/shampoo-tresemme-bajo-poo-nutricion-400-ml/p",
"https://www.vea.com.ar/jabon-en-barra-palmolive-naturals-oliva-y-aloe-125-gr-pack-3-u-2/p",
"https://www.vea.com.ar/desodorante-antitranspirante-rexona-invisible-en-aerosol-150-ml/p",
"https://www.vea.com.ar/desodorante-femenino-antitranspirante-nivea-powder-150-ml/p",
"https://www.vea.com.ar/suavizante-para-ropa-comfort-clasico-900-ml/p",
"https://www.vea.com.ar/limpiador-procenex-repuesto-420-ml/p",
"https://www.vea.com.ar/limpiador-liquido-cif-antigrasa-biodegradable-500-ml-gatillo/p",
"https://www.vea.com.ar/limpiador-liquido-cif-antigrasa-biodegradable-450-ml-doypack/p",
"https://www.vea.com.ar/desodorante-de-ambiente-poett-frescura-de-lavanda-360-ml/p",
"https://www.vea.com.ar/ayudin-desinfectante-aerosol-original-332ml/p",
"https://www.vea.com.ar/aromatizante-de-ambientes-glade-manana-de-campo-en-aerosol-360ml/p",
"https://www.vea.com.ar/insecticida-selton-mata-moscas-y-mosquitos-sin-olor-a-quimicos-aerosol-360-cm3/p",
"https://www.vea.com.ar/insecticida-raid-mata-moscas-y-mosquitos-sin-olor-en-aerosol-360-cc/p",
"https://www.vea.com.ar/rollo-de-cocina-campanita-classic-x-3-un/p",
"https://www.vea.com.ar/rollo-de-cocina-sussex-3x50-clasico/p",
"https://www.vea.com.ar/rollo-de-cocina-3x50-panos-vea/p",
"https://www.vea.com.ar/cocina-volcan-blanco-a-gas-89644vm/p",
"https://www.vea.com.ar/cocina-orbis-macrovision-858bc3m-blanca/p",
"https://www.vea.com.ar/heladera-ciclica-patrick-hpk135m00b01-277l-blanca/p",
"https://www.vea.com.ar/heladera-electrolux-no-frost-blanca-269-l/p",
"https://www.vea.com.ar/termotanque-saiar-elec-pol-85l-tepco85esarik2/p",
"https://www.vea.com.ar/termotanque-gas-rheem-80-l/p",
"https://www.vea.com.ar/aire-acondicionado-bgh-blanco-frio-calor-3450-w/p",
"https://www.vea.com.ar/aire-acondicionado-philco-phs32ha3an-3350-blanco-fc/p",
"https://www.vea.com.ar/lavarropas-drean-7-kg-eea/p",
"https://www.vea.com.ar/lavarropas-aurora-7510-carga-frontal-7k/p",
"https://www.vea.com.ar/leche-la-serenisima-uat-parcialmente-descremada-liviana-1-l/p",
"https://www.vea.com.ar/leche-ls-uat-entera-clasica-3brik-1l/p",
"https://www.vea.com.ar/leche-en-polvo-nido-3-prebio-1-leche-800g/p",
"https://www.vea.com.ar/papel-higienico-campanita-doble-hoja-x-4un/p",
"https://www.vea.com.ar/papel-higienico-elite-hoja-simple-30-m-4-u/p",
"https://www.vea.com.ar/papel-higienico-felpita-hoja-simple/p",
"https://www.vea.com.ar/manzana-5/p",
"https://www.vea.com.ar/banana-x-kg/p",
"https://www.vea.com.ar/pera-6/p",
"https://www.vea.com.ar/naranja-ombligo-por-kg/p",
"https://www.vea.com.ar/limon/p",
"https://www.vea.com.ar/mandarina-6/p",
"https://www.vea.com.ar/pomelo-por-kg/p",
"https://www.vea.com.ar/cebolla-superior-por-kg/p",
"https://www.vea.com.ar/papa-negra-granel/p",
"https://www.vea.com.ar/tomate-redondo-comercial/p",
"https://www.vea.com.ar/zanahoria/p",
"https://www.vea.com.ar/zapallo-coreano/p",
"https://www.vea.com.ar/pimiento-rojo-superior/p",
"https://www.vea.com.ar/acelga-8/p",
"https://www.vea.com.ar/lechuga-7/p",
"https://www.vea.com.ar/remolacha-por-kg/p",
"https://www.vea.com.ar/azucar-chango/p",
"https://www.vea.com.ar/azucar-domino-1-kg/p",
"https://www.vea.com.ar/endulzante-hileret-clasico-x-50-sobrecitos/p",
"https://www.vea.com.ar/edulequalsweetclassobres-con-zinc-40-un/p",
"https://www.vea.com.ar/endulzante-hileret-sweet-forte-x-50-sobrecito/p",
"https://www.vea.com.ar/mayonesa-cada-dia-light-500-gr/p",
"https://www.vea.com.ar/mayonesa-hellmanns-475g/p",
"https://www.vea.com.ar/lavandina-ayudin/p",
"https://www.vea.com.ar/lavandina-queruclor-conc-premium-1l/p",
"https://www.vea.com.ar/lavandina-ayudin-triple-poder-lavanda-2-l/p",
"https://www.vea.com.ar/lavandina-querubin/p",
"https://www.vea.com.ar/toallas-higienicas-always-suave-maxi-proteccion-16-unidades/p",
"https://www.vea.com.ar/toallas-femeninas-siempre-libre-especial-adapt-con-alas-x-16-u/p",
"https://www.vea.com.ar/toal-fem-ladysoft-normal-tela-suax16/p",
"https://www.vea.com.ar/toalla-femenina-kotex-esencial-x-16-u/p",
"https://www.vea.com.ar/yerba-mate-playadito-suave-x500gr/p",
"https://www.vea.com.ar/yerba-mate-rosamonte-con-palo/p",
"https://www.vea.com.ar/te-ngr-clasic-green-hills-momentos-50sac/p",
"https://www.vea.com.ar/te-vea-en-saquitos-x-50-un/p",
"https://www.vea.com.ar/gaseosa-cunnington-cola-2250cc/p",
"https://www.vea.com.ar/gaseosa-cordoba-cormillot-cola-2-25-lts/p",
"https://www.vea.com.ar/jugo-citric-refrigerado-manzana-1-l/p",
"https://www.vea.com.ar/jugos-tutti-multifruta-2/p",
"https://www.vea.com.ar/panal-huggies-triple-protecc-m-x26un/p",
"https://www.vea.com.ar/panal-babysec-ultra-m-x-26-u/p",
"https://www.vea.com.ar/jabon-de-glicerina-veritas/p",
"https://www.vea.com.ar/jabon-liquido-algabo-5/p",
"https://www.vea.com.ar/helado-sei-tu-palito-bombon-x6u/p",
"https://www.vea.com.ar/helado-balde-noel-ddlfllachoc-1kg/p",
"https://www.vea.com.ar/chocolate-kinder-100-gr/p",
"https://www.vea.com.ar/caramelos-sugus-masticables-frutales-x-150-gr/p",
"https://www.vea.com.ar/filet-de-merluzaj-x-kg/p",
"https://www.vea.com.ar/mejillones-pelado-250-gr/p",
"https://www.vea.com.ar/langostinos-pelados-cocidos-superbe/p",
"https://www.vea.com.ar/kani-kama-santa-elena-2/p",
"https://www.vea.com.ar/medallones-de-merluza-rebozados-portobelo-500-gr/p",
"https://www.vea.com.ar/manteca-tonadita-c-vitamina-200g/p",
"https://www.vea.com.ar/manteca-multivitaminas-la-serenisima-200gr/p",
"https://www.vea.com.ar/asado-de-novillito-ca/p",
"https://www.vea.com.ar/vacio-de-novillito-ca/p",
"https://www.vea.com.ar/matambre-3/p",
"https://www.vea.com.ar/milanesa-cuadrada-por-kg/p",
"https://www.vea.com.ar/milanesa-bola-de-lomo-4/p",
"https://www.vea.com.ar/tapa-de-asado-por-kg-2/p",
"https://www.vea.com.ar/carnaza-comun-por-kg/p",
"https://www.vea.com.ar/falda-por-kg/p",
"https://www.vea.com.ar/roast-beef-trozo-por-kg/p",
"https://www.vea.com.ar/carne-picada-promo-de-novillito/p",
"https://www.vea.com.ar/carre-de-cerdo-deshuesado-congelado/p",
"https://www.vea.com.ar/milanesa-nalga-5/p",
"https://www.vea.com.ar/bife-de-chorizo-2/p",
"https://www.vea.com.ar/higado/p",
"https://www.vea.com.ar/paleta-en-trozo-de-novillito/p",
"https://www.vea.com.ar/flautita-p/p",
"https://www.vea.com.ar/pan-lacteado-lactal-de-mesa-x-335grs/p",
"https://www.vea.com.ar/pan-lacteado-dona-noly-2/p",
"https://www.vea.com.ar/arroz-dos-hermanos-grano-largo-fino-1-kg/p",
"https://www.vea.com.ar/arroz-integral-gallo-x1-kg/p",
"https://www.vea.com.ar/harina-canuelas-ultra-ref-000-vit-d-1kg/p",
"https://www.vea.com.ar/harina-presto-pronta-de-maiz-2/p",
"https://www.vea.com.ar/semola-clasica-con-calcio-vitina-x500-gr/p",
"https://www.vea.com.ar/pan-rallado-preferido-x1-kg/p",
"https://www.vea.com.ar/fideos-marolio-spaghetti-secos-c-curcuma-x500g/p",
"https://www.vea.com.ar/fideos-spaghetti-lucchetti-x500-gr/p",
"https://www.vea.com.ar/fideos-marolio-tirabuzon-x-500-gr-fideos-marolio-tirabuzon-x-500-gr/p",
"https://www.vea.com.ar/fideos-tirabuzon-lucchetti-x500-gr/p",
"https://www.vea.com.ar/fideos-marolio-mostachol/p",
"https://www.vea.com.ar/fideos-mostachol-lucchetti-x500-gr/p",
"https://www.vea.com.ar/prepizza-x-1-un-3/p",
"https://www.vea.com.ar/ravioles-p-y-v-via-vespucci-x-500gr/p",
"https://www.vea.com.ar/ravioles-con-ricota-villa-d-a-gr-y-espinaca-500-gr/p",
"https://www.vea.com.ar/tapas-p-empanadas-dona-noly-criollas-x-330-g/p",
"https://www.vea.com.ar/tapas-empanadas-punto-pasta-criollas-horno-freir-x-300grs/p",
"https://www.vea.com.ar/tapa-empanadas-horno-villa-d-a-gr-330-gr-blister-12-u/p",
"https://www.vea.com.ar/tapa-pascualina-criolla-dona-noly-400-g/p",
"https://www.vea.com.ar/tapas-pascualinas-punto-pasta-hojaldradas-x-400grs/p",
"https://www.vea.com.ar/talitas-don-satur-x140gr/p",
"https://www.vea.com.ar/tostadas-clasicas-riera-2/p",
"https://www.vea.com.ar/leche-ls-uat-entera-clasica-3brik-1l/p",
"https://www.vea.com.ar/leche-la-serenisima-uat-parcialmente-descremada-liviana-1-l/p",
"https://www.vea.com.ar/leche-entera-uat-tregar-x-1-litro/p",
"https://www.vea.com.ar/leche-uat-desc-1tregar-1l/p",
"https://www.vea.com.ar/desodorante-de-ambiente-poett-espiritu-play-360-ml/p",
"https://www.vea.com.ar/yerba-mate-rosamonte-con-palo-2/p",
"https://www.vea.com.ar/jugos-tutti/p",
"https://www.vea.com.ar/ravioles-ricota-via-vespucci-x-500gr/p",
"https://www.vea.com.ar/asado-de-novillito/p",
"https://www.vea.com.ar/asado-del-centro-de-novillito/p",
"https://www.vea.com.ar/vacio-de-novillito-2/p",
"https://www.vea.com.ar/vacio-de-novillito/p",
"https://www.vea.com.ar/cuadrada-en-milanesa-de-novillito/p",
"https://www.vea.com.ar/bola-de-lomo-promo-x-kg/p",
"https://www.vea.com.ar/falda-de-novillito/p",
"https://www.vea.com.ar/carne-picada-promo-de-novillito/p",
"https://www.vea.com.ar/vino-coliman-clasico-tinto/p",
"https://www.vea.com.ar/vino-fino-colon-malbec-x-750-cc/p",
"https://www.vea.com.ar/cerveza-schneider-rubia-1lt/p",
"https://www.vea.com.ar/cerveza-palermo-1lt-retornable/p",
"https://www.vea.com.ar/cerveza-andes-rubia-ret-1lt/p",
"https://www.vea.com.ar/ravioles-pollo-via-vespucci-x-1kg/p",
"https://www.vea.com.ar/leche-parcialmente-descremada-1-armonia-sachet-1-l/p",
"https://www.vea.com.ar/milanesa-nalga-5/p",
"https://www.vea.com.ar/cuadril-de-novillito/p",
"https://www.vea.com.ar/entrana-2/p",
"https://www.vea.com.ar/paleta-en-trozo-de-novillito/p",
"https://www.vea.com.ar/mayonesa-hellmanns-475g/p",
"https://www.vea.com.ar/queso-sardo-la-paulina/p",
"https://www.vea.com.ar/queso-sardo-la-serenisima-paq-x-kg/p"}