import qgis.core
import os
from qgis.core import *
from qgis.core import QgsProject
from optparse import OptionParser

QML = '/styles/ch.so.agi.av.grundstuecke.rechtskraeftige_v3.qml'


def run(output_file, raster_layers, vector_layers):
    # QgsApplication.setPrefixPath("/usr/bin/qgis", True)
    qgs = QgsApplication([], False)
    qgs.initQgis()
    project = QgsProject()
    project.write('/data/mock.qgs')

    for i in range(vector_layers):
        uri = QgsDataSourceUri()
        uri.setConnection("postgis", "5432", "gdwh", "postgres", "password")
        uri.setDataSource("agi_mopublic_pub", "mopublic_grundstueck", "geometrie", '', 't_id')
        uri.setSrid("2056")
        uri.setGeometryColumn("geometrie")
        uri.setKeyColumn("t_id")
        vlayer = QgsVectorLayer(uri.uri(False), "Grundstueck {}".format(i), "postgres")
        request = QgsFeatureRequest()
        request.setLimit(2)
        features = vlayer.getFeatures(request)
        for f in features:
            print(f.id)
        # if not vlayer.isValid():
        #     raise IOError('Layer was not valid!')
        vlayer.loadNamedStyle(QML)
        project.addMapLayer(vlayer)
    
    for i in range(raster_layers):
        file_path = "/data/ch.so.agi.orthofoto_2017.rgb/orthofoto_2017_rgb_12_5cm.vrt"
        rlayer = QgsRasterLayer(file_path, 'Orthophoto {}'.format(i))
        if not vlayer.isValid():
            raise IOError('Layer was not valid!')
        vlayer.loadNamedStyle('/styles/ch.so.agi.av.grundstuecke.rechtskraeftige_v3.qml')
        project.addMapLayer(rlayer)

    project.write()
    qgs.exitQgis()

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
