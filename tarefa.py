class Tarefa:
    def __init__(self, task_id, titulo, descricao, status, dt_inicio, comentarios, dificuldade):
        self.task_id = task_id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.dt_inicio = dt_inicio
        self.comentarios = comentarios
        self.dificuldade = dificuldade

    def to_json(self):
        return {
            "task_id": self.task_id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "dt_inicio": self.dt_inicio,
            "comentarios": self.comentarios,
            "dificuldade": self.dificuldade
        }