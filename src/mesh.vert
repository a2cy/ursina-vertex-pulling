#version 430

struct Vertex {
  float position[3];
};

layout(std430) buffer VertexBuffer {
  Vertex vertices[];
};

uniform mat4 p3d_ModelViewProjectionMatrix;

void main() {
    vec4 vertex = vec4(vertices[gl_VertexID].position[0], vertices[gl_VertexID].position[1], vertices[gl_VertexID].position[2], 1);

    gl_Position = p3d_ModelViewProjectionMatrix * vertex;
}