#version 150

uniform mat4 p3d_ModelViewProjectionMatrix;

vec3[] vertices = vec3[36](
  vec3(-0.5, -0.5, -0.5),
  vec3(0.5, -0.5, -0.5),
  vec3(0.5, 0.5, -0.5),
  vec3(0.5, 0.5, -0.5),
  vec3(-0.5, 0.5, -0.5),
  vec3(-0.5, -0.5, -0.5),
  vec3(-0.5, -0.5, 0.5),
  vec3(-0.5, -0.5, -0.5),
  vec3(-0.5, 0.5, -0.5),
  vec3(-0.5, 0.5, -0.5),
  vec3(-0.5, 0.5, 0.5),
  vec3(-0.5, -0.5, 0.5),
  vec3(0.5, -0.5, 0.5),
  vec3(-0.5, -0.5, 0.5),
  vec3(-0.5, 0.5, 0.5),
  vec3(-0.5, 0.5, 0.5),
  vec3(0.5, 0.5, 0.5),
  vec3(0.5, -0.5, 0.5),
  vec3(0.5, -0.5, -0.5),
  vec3(0.5, -0.5, 0.5),
  vec3(0.5, 0.5, 0.5),
  vec3(0.5, 0.5, 0.5),
  vec3(0.5, 0.5, -0.5),
  vec3(0.5, -0.5, -0.5),
  vec3(0.5, 0.5, 0.5),
  vec3(-0.5, 0.5, 0.5),
  vec3(-0.5, 0.5, -0.5),
  vec3(-0.5, 0.5, -0.5),
  vec3(0.5, 0.5, -0.5),
  vec3(0.5, 0.5, 0.5),
  vec3(0.5, -0.5, -0.5),
  vec3(-0.5, -0.5, -0.5),
  vec3(-0.5, -0.5, 0.5),
  vec3(-0.5, -0.5, 0.5),
  vec3(0.5, -0.5, 0.5),
  vec3(0.5, -0.5, -0.5)
);

void main() {
    vec4 vertex = vec4(vertices[gl_VertexID].x, vertices[gl_VertexID].y, vertices[gl_VertexID].z, 1);

    gl_Position = p3d_ModelViewProjectionMatrix * vertex;
}