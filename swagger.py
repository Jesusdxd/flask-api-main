swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Api 101 by Alexis",
        "description": "Documentación de la API 101 y sus opreaciones CRUD en swagger",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": [
        "http"
    ],
    "paths":{
        "/api/usuarios":{
            "get": {
                "summary": "Obtener lista de usuarios",
                "description": "Obtener todos los usuarios",
                "responses" : {
                    "200": {
                        "description": "Lista de usuarios",
                        "schema" : {
                            "type": "array",
                            "items": {
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
                                    "nombre": {
                                        "type": "string"
                                    },
                                    "email": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "summary": "Agregar un nuevo usuario",
                "description": "Agregar un usuario con los campos 'nombre' y 'email'.",
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "properties" : {
                                "nombre": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Usuario agregado exitosamente"
                    }
                }
            }
        },
        "/api/usuarios/{id}": {
            "put": {
                "summary": "Actualizar un usuario",
                "description": "Actualizar un usuario proporcionando su id",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "type": "integer",
                        "required": True,
                        "description": "Id del usuario a actualizar"
                    },
                    {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "properties": {
                                "nombre": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Usuario actualizado exitosamente"
                    },
                    "404": {
                        "description": "Usuario no encontrado"
                    }
                }
            },
            "delete": {
                "summary": "Eliminar un usuario",
                "description": "Eliminar un usuario proporcionando su id",
                    "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "type": "integer",
                        "required": True,
                        "description": "Id del usuario a eliminar"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Usuario eliminado exitosamente"
                    },
                    "404": {
                        "description": "Usuario no encontrado"
                    }
                }
            }
        }
    }
}