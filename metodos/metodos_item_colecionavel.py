from flask import request, jsonify
from modelos.itens_colecionaveis import ItensColecionaveis
from modelos.tipos_item import TipoItemColecionavel

from extensions import db

"""
class ItensColecionaveis(db.Model):
    __tablename__ = 'itens_colecionaveis'

    id_item: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tipo = mapped_column(ForeignKey("tipo_item_colecionavel.id_tipo"))
    nome_item: Mapped[str] = mapped_column(String(50), nullable=False, default="Nome não definido")
    valor_item: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)

class TipoItemColecionavel (db.Model):
    __tablename__ = 'tipo_item_colecionavel'

    id_tipo = mapped_column(Integer, primary_key=True, autoincrement=True)
    tipo_item = mapped_column(String(30), nullable=False, default="Sem classificação")
"""

def receber_requisicao_sem_id():
    dados = request.get_json()

    nome_item = dados.get("nome_item")
    tipo_item = dados.get("tipo_item")
    valor_item = dados.get("valor_item")

    validar_requisicao_itens_sem_id(nome_item, tipo_item, valor_item)

    return nome_item, tipo_item, valor_item

def validar_requisicao_itens_sem_id(nome_item,tipo_item,valor_item):
    if not nome_item:
        return jsonify({"Erro":"Nome do item é obrigatório"}), 400
    if not tipo_item:
        return jsonify({"Erro":"Tipo do item é obrigatório"}), 400
    if valor_item < 0.00:
        return jsonify({"Erro":"Não permitido valor negativo"}), 400

def receber_requisicao_completa():
    nome_item, tipo_item, valor_item = receber_requisicao_sem_id()
    id_item = request.get_json().get("id_item")

    if not id_item:
        return jsonify({"Erro":"ID de identificação necessário"}), 400

    return id_item, tipo_item, nome_item, valor_item

def verifica_tipo_existente(tipo_requisicao):
    select_tipo_existente = db.select(TipoItemColecionavel).filter_by(tipo_item=tipo_requisicao)
    tipo_existe = db.session.execute(select_tipo_existente).scalar_one_or_none()
    if tipo_existe is None:
        return jsonify({"Erro": "Tipo de item não existente"}),409


def metodo_cadastrar_item():

    nome_item_requisicao, tipo_item_requisicao, valor_item_requisicao = receber_requisicao_sem_id()

    try:
        item_cadastrado = ItensColecionaveis(
            tipo = tipo_item_requisicao,
            nome_item = nome_item_requisicao,
            valor_item = valor_item_requisicao
        )

        select_tipo_existente = db.select(TipoItemColecionavel).filter_by(tipo_item=tipo_item_requisicao)
        tipo_existente = db.session.execute(select_tipo_existente).scalar_one_or_none()
        if tipo_existente is None:
            return jsonify({"Erro":"Tipo de item não cadastrado na base"}), 409

        select_item_colecionavel = db.select(ItensColecionaveis).filter_by(tipo=tipo_item_requisicao, nome_item=nome_item_requisicao)
        item_existente = db.session.execute(select_item_colecionavel).scalar_one_or_none()
        if item_existente:
            return jsonify({"Erro":"Item já cadastrado"}), 409

        db.session.add(item_cadastrado)
        db.session.commit()

        resposta =[{"tipo":tipo_item_requisicao, 
                    "nome_item":nome_item_requisicao, 
                    "valor_item":valor_item_requisicao,
                    "mensagem": "Item cadastrado com sucesso"
                    }]       

        return jsonify(resposta), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"Erro": "Erro nao identificado:" + str(e)}), 400

def metodo_consultar_itens_colecionaveis():
    try:
        select_todos_itens_colecionaveis = db.select(ItensColecionaveis).order_by(ItensColecionaveis.id_tipo)
        todos_itens = db.session.execute(select_todos_itens_colecionaveis).scalars().all()
    
        resposta = [
            {"id_item": item.id_item, 
             "tipo": item.tipo,
             "nome_item":item.nome_item,
             "valor_item":item.valor_item}
             for item in todos_itens
            ]
        return jsonify(resposta), 200
        
    except Exception as e:
        return jsonify({"Erro": "Erro nao identificado:" + str(e)}), 400

def metodo_consultar_itens_colecionaveis_por_tipo(tipo_de_item):

    tipo_requisicao = tipo_de_item

    try:
        verifica_tipo_existente(tipo_requisicao)

        select_todos_itens_colecionaveis_por_tipo = db.select(ItensColecionaveis).filter_by(tipo=tipo_requisicao)
        todos_itens = db.session.execute(select_todos_itens_colecionaveis_por_tipo).scalars().all()
    
        resposta = [
            {"id_item": item.id_item,
             "tipo": item.tipo,
             "nome_item":item.nome_item,
             "valor_item":item.valor_item} 
             for item in todos_itens
            ]
        return jsonify(resposta), 200
        
    except Exception as e:
        return jsonify({"Erro": "Erro nao identificado:" + str(e)}), 400

def metodo_alterar_item_colecionável():

    id_item_requisicao, tipo_item_requisicao, nome_item_requisicao, valor_item_requisicao = receber_requisicao_completa()

    try:
        verifica_tipo_existente(tipo_item_requisicao)

        select_item_por_id = db.select(ItensColecionaveis).filter_by(id_item=id_item_requisicao)
        item_a_alterar = db.session.execute(select_item_por_id).scalar_one_or_none()
        if item_a_alterar is None:
            return jsonify({"Erro": "Item não encontrado"}), 409

        item_a_alterar.tipo = tipo_item_requisicao
        item_a_alterar.nome_item = nome_item_requisicao
        item_a_alterar.valor_item = valor_item_requisicao

        db.session.commit()

        resposta = [{
            "id_item":item_a_alterar.id_item,
            "tipo":tipo_item_requisicao,
            "nome_item":nome_item_requisicao,
            "valor_item": valor_item_requisicao,
            "mensagem":"Item alterado com sucesso"
            }]

        return jsonify(resposta), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"Erro": "Erro nao identificado:" + str(e)}), 400

def metodo_deletar_item_colecionável():

    id_item_requisicao, tipo_item_requisicao, nome_item_requisicao, valor_item_requisicao = receber_requisicao_completa()

    try:
        verifica_tipo_existente(tipo_item_requisicao)

        select_item_colecionavel = db.select(ItensColecionaveis).filter_by(tipo=id_item_requisicao)
        item_a_ser_deletado = db.session.execute(select_item_colecionavel).scalar_one_or_none()

        if item_a_ser_deletado.nome_item != nome_item_requisicao:
            return jsonify({"Erro":"Verifique o nome do item informado"}), 404

        if item_a_ser_deletado.tipo != tipo_item_requisicao:
            return jsonify({"Erro":"Verifique o tipo do item informado"}), 404

        if item_a_ser_deletado.valor_item_requisicao != valor_item_requisicao:
            return jsonify({"Erro":"Verifique o valor do item informado"}), 404
        
        db.session.delete(item_a_ser_deletado) 
        db.session.commit()

        resposta = [{"tipo":tipo_item_requisicao,
                     "nome_item":nome_item_requisicao,
                     "valor_item":valor_item_requisicao,
                     "mensagem": "Item deletado com sucesso"
                     }]
            
        return jsonify(resposta), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"Erro": "Erro nao identificado:" + str(e)}), 400 