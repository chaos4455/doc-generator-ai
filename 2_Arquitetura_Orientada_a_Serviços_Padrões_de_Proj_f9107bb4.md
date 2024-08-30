## **Padrões de Projeto para Camadas de Serviço e Repositório**

**Introdução:**

A arquitetura orientada a serviços (SOA) é um estilo arquitetônico que decompõe um sistema em serviços reusáveis e independentes. As camadas de serviço e repositório são componentes essenciais de uma arquitetura SOA.

**Camada de Serviço**

**Objetivo:**

* Encapsular a lógica de negócios e o acesso a dados.
* Fornecer uma interface consistente para clientes.

**Padrões de Projeto:**

* **Service Locator:** Cria um local central para gerenciar o acesso a serviços.
* **Factory Method:** Cria objetos de serviço sem especificar a classe concreta.
* **Decorator:** Adiciona funcionalidade adicional a um serviço sem alterar sua interface.

**Exemplo:**

```
// Service Locator
public class ServiceLocator {
    private static Map<String, Object> services = new HashMap<>();
    public static Object get(String name) {
        return services.get(name);
    }
    public static void register(String name, Object service) {
        services.put(name, service);
    }
}

// Factory Method
public abstract class ServiceFactory {
    public abstract Service create();
}
public class MyServiceFactory extends ServiceFactory {
    @Override
    public Service create() {
        return new MyService();
    }
}

// Decorator
public abstract class ServiceDecorator implements Service {
    protected Service service;
    public ServiceDecorator(Service service) {
        this.service = service;
    }
}
public class CachingServiceDecorator extends ServiceDecorator {
    private Map<String, Object> cache = new HashMap<>();
    @Override
    public Object get(String key) {
        Object value = cache.get(key);
        if (value == null) {
            value = service.get(key);
            cache.put(key, value);
        }
        return value;
    }
}
```

**Camada de Repositório**

**Objetivo:**

* Encapsular o acesso a dados.
* Fornecer uma interface consistente para serviços.

**Padrões de Projeto:**

* **Repository:** Define uma interface para acessar dados.
* **UnitOfWork:** Gerencia uma transação de banco de dados.
* **Factory Method:** Cria objetos de repositório sem especificar a classe concreta.

**Exemplo:**

```
// Repository
public interface Repository<T> {
    T find(Object id);
    List<T> findAll();
    void save(T entity);
    void delete(T entity);
}

// UnitOfWork
public interface UnitOfWork {
    void beginTransaction();
    void commitTransaction();
    void rollbackTransaction();
}

// Factory Method
public abstract class RepositoryFactory {
    public abstract Repository<T> create();
}
public class MyRepositoryFactory extends RepositoryFactory {
    @Override
    public Repository<T> create() {
        return new MyRepository();
    }
}
```

**Conclusão:**

Os padrões de projeto apresentados neste manual ajudam a implementar camadas de serviço e repositório efetivas em uma arquitetura SOA. Eles promovem encapsulamento, desacoplamento e reutilização, resultando em sistemas escaláveis e manuteníveis.