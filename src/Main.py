
import TipoDeCambio, TasaDiaria, BolsaDeValores, Archivo
from decouple import config

if __name__ == '__main__':

        bvl = BolsaDeValores.BVL()
        bvl.iniciar_busqueda('https://www.bvl.com.pe/productos/publicaciones')
        bvl.error()
        indices_BVL=bvl.recolectar_datos()

        sbs_T_C = TipoDeCambio.SBSTipoCambio()
        sbs_T_C.iniciar_busqueda('https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx')
        indices_tipo_cambio = sbs_T_C.recolectar_datos()

        sbs_td = TasaDiaria.SBSTasaDiaria()
        #sbs_td.iniciar_busqueda(config('TASA_DIARIA'))
        sbs_td.iniciar_busqueda('https://www.sbs.gob.pe/app/stats/TasaDiaria_1.asp')
        indices_tasa_diaria = sbs_td.recolectar_datos()

        Archivo.Archivo().archivandoDatos(indices_tipo_cambio,indices_tasa_diaria,indices_BVL)
