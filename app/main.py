from app.currency_api import get_dollar_exchange_rate
from app.task_manager import add_task, list_tasks, complete_task, remove_task


print("\n=== ATUALIZAÇÕES DO DIA ===")
print(get_dollar_exchange_rate())


def show_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")


def main():
    while True:
        show_menu()
        choice = input("Escolha uma opção: ")

        try:
            if choice == "1":
                title = input("Digite a tarefa: ")
                add_task(title)
                print("Tarefa adicionada!")

            elif choice == "2":
                tasks = list_tasks()
                if not tasks:
                    print("Nenhuma tarefa.")
                for i, task in enumerate(tasks):
                    status = "✔" if task["done"] else "✘"
                    print(f"{i} - {task['title']} [{status}]")

            elif choice == "3":
                index = int(input("Número da tarefa: "))
                complete_task(index)
                print("Tarefa concluída!")

            elif choice == "4":
                index = int(input("Número da tarefa: "))
                remove_task(index)
                print("Tarefa removida!")

            elif choice == "5":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
