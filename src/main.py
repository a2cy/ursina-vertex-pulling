import numpy as np

from ursina import Ursina, Shader, Entity, EditorCamera, load_model
from panda3d.core import NodePath, Geom, GeomNode, GeomVertexFormat, GeomVertexData, GeomTriangles, OmniBoundingVolume, ShaderBuffer


class Mesh(NodePath):

    vertex_format = GeomVertexFormat.get_empty()

    def __init__(self, vertex_count, **kwargs):
        super().__init__("mesh")

        self.geom_node = GeomNode("geom_node")
        self.attach_new_node(self.geom_node)

        v_data = GeomVertexData("vertex_data", self.vertex_format, Geom.UH_static)

        prim = GeomTriangles(Geom.UH_static)
        prim.add_next_vertices(vertex_count//3)

        geom = Geom(v_data)
        geom.addPrimitive(prim)
        geom.set_bounds(OmniBoundingVolume())
        self.geom_node.add_geom(geom)

        for key, value in kwargs.items():
            setattr(self, key, value)


if __name__ == "__main__":
    app = Ursina(borderless=False)

    texture_shader = Shader.load(Shader.GLSL, vertex="mesh.vert", fragment="mesh.frag")

    model = load_model("cube", use_deepcopy=True)

    vertices = np.array(model.vertices, dtype=np.single).ravel()

    vertex_buffer = ShaderBuffer("vertex_buffer", vertices.tobytes(), Geom.UH_static)

    chunk = Entity(model=Mesh(vertices.shape[0]), shader=texture_shader)
    chunk.set_shader_input("VertexBuffer", vertex_buffer)

    EditorCamera()

    app.run()

