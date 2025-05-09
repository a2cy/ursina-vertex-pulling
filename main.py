from ursina import Ursina, Shader, Entity, EditorCamera
from panda3d.core import NodePath, Geom, GeomNode, GeomVertexFormat, GeomVertexData, GeomTriangles, OmniBoundingVolume


class Mesh(NodePath):

    vertex_format = GeomVertexFormat.get_empty()

    def __init__(self, vertex_count, **kwargs):
        super().__init__("mesh")

        self.geom_node = GeomNode("geom_node")
        self.attach_new_node(self.geom_node)

        v_data = GeomVertexData("vertex_data", self.vertex_format, Geom.UH_static)

        prim = GeomTriangles(Geom.UH_static)
        prim.add_next_vertices(vertex_count)

        geom = Geom(v_data)
        geom.addPrimitive(prim)
        geom.set_bounds(OmniBoundingVolume())
        self.geom_node.add_geom(geom)

        for key, value in kwargs.items():
            setattr(self, key, value)


if __name__ == "__main__":
    app = Ursina(borderless=False)

    texture_shader = Shader.load(Shader.GLSL, vertex="mesh.vert", fragment="mesh.frag")

    chunk = Entity(model=Mesh(36), shader=texture_shader)

    EditorCamera()

    app.run()

