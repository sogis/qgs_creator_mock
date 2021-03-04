import qgis.core
from qgis.core import *
from qgis.core import QgsProject
from PyQt4.QtCore import QFileInfo
from optparse import OptionParser


def run(output_file, layer_count):
    QgsApplication.setPrefixPath("/usr/bin/qgis", True)
    qgs = QgsApplication([], False)
    qgs.initQgis()
    project = QgsProject.instance()
    project.write(QFileInfo('/data/mock.qgs'))
    reg = QgsMapLayerRegistry.instance()

    for i in range(layer_count):
        vlayer = QgsVectorLayer(
            "/data/input.shp",
            "Test {}".format(i),
            "ogr"
        )
        if not vlayer.isValid():
            raise IOError('Layer was not valid!')
        reg.addMapLayer(vlayer)
        project.layerTreeRoot().addLayer(vlayer)

    project.write()
    qgs.exitQgis()

def main():
    parser = OptionParser(usage="usage: %prog [options]")
    parser.add_option("-o", "--output_file",
                      dest="output_file",
                      default='/data/mock.qgs',
                      help="Set a different output file if necessary")
    parser.add_option("-l", "--layer_count",
                      dest="layer_count",
                      default=1000,
                      help="Number of layers added to the QGS file.",)
    (options, args) = parser.parse_args()

    run(options.output_file, options.layer_count)

if __name__ == '__main__':
    main()
