import qgis.core
import os
from qgis.core import *
from optparse import OptionParser

QML = '/styles/ch.so.agi.av.grundstuecke.rechtskraeftige_v3.qml'
db_host = 'postgis'
db_port = '5432'
db = 'gdwh'
db_user = 'postgres'
db_pw = 'password'
db_schema = 'agi_mopublic_pub'
db_table = 'mopublic_grundstueck'
geometry_column = 'geometrie'
primary_key_column = 't_id'



def run(output_file, raster_layers, vector_layers):
    qgs = QgsApplication([], False)
    qgs.initQgis()
    project = QgsProject()

    for i in range(vector_layers):
        uri = QgsDataSourceUri()
        uri.setConnection(db_host, db_port, db, db_user, db_pw)
        uri.setDataSource(db_schema, db_table, geometry_column, '', primary_key_column)
        uri.setUseEstimatedMetadata(True)
        vlayer = QgsVectorLayer(uri.uri(False), "Grundstueck {}".format(i), "postgres")
        if not vlayer.isValid():
            raise IOError('Layer was not valid!')
        vlayer.loadNamedStyle(QML)
        project.addMapLayer(vlayer)
    
    for i in range(raster_layers):
        file_path = "/data/ch.so.agi.orthofoto_2017.rgb/orthofoto_2017_rgb_12_5cm.vrt"
        rlayer = QgsRasterLayer(file_path, 'Orthophoto {}'.format(i), 'gdal')
        if not vlayer.isValid():
            raise IOError('Layer was not valid!')
        project.addMapLayer(rlayer)
    project.write('/data/mock.qgs')

def main():
    parser = OptionParser(usage="usage: %prog [options]")
    parser.add_option(
        "-o", "--output_file",
        dest="output_file",
        default='/data/mock.qgs',
        help="Set a different output file if necessary"
    )
    parser.add_option(
        "-r", "--raster_layers",
        dest="raster_layers",
        default=100,
        type="int",
        help="Percentage of raster layers added."
    )
    parser.add_option(
        "-v", "--vector_layers",
        dest="vector_layers",
        default=400,
        type="int",
        help="Percentage of vector layers added."
    )
    
    (options, args) = parser.parse_args()

    run(options.output_file, options.raster_layers, options.vector_layers)

if __name__ == '__main__':
    main()
