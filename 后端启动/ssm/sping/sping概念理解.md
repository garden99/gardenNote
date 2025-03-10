# 1. **控制反转（IoC, Inversion of Control）**

- **定义**：IoC 是 Spring 的核心思想之一。它将对象的创建和依赖关系的管理从应用程序代码中转移到 Spring 容器中。

- **实现方式**：通过依赖注入（DI, Dependency Injection）实现。

- **优点**：降低了代码的耦合度，提高了代码的可测试性和可维护性。

## 代码

```java
    // 传统方式：手动创建对象
UserService userService = new UserServiceImpl();
    
// Spring 方式：通过 IoC 容器管理对象
@Autowired
UserService userService;
```

# 2. **依赖注入（DI, Dependency Injection）**

- **定义**：DI 是 IoC 的一种实现方式，Spring 容器负责将依赖对象注入到目标对象中。

- **注入方式**：
  
  - **构造器注入**：通过构造方法注入依赖。
  
  - **Setter 注入**：通过 Setter 方法注入依赖。
  
  - **字段注入**：通过 `@Autowired` 注解直接注入字段（不推荐）。
  
  ## 代码

```java
// 构造器注入
public class UserService {
    private UserRepository userRepository;

    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}

// Setter 注入
public class UserService {
    private UserRepository userRepository;

    @Autowired
    public void setUserRepository(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```

# 3. **Spring 容器**

- **定义**：Spring 容器是 Spring 框架的核心，负责管理对象的生命周期和依赖关系。

- **主要实现**：
  
  - **BeanFactory**：基础容器，提供基本的 DI 支持。
  
  - **ApplicationContext**：扩展了 `BeanFactory`，提供了更多企业级功能（如国际化、事件传播等）。

## 代码

```java
// 创建 ApplicationContext
ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);

// 从容器中获取 Bean 类获取不适用多例模式
UserService userService = context.getBean(UserService.class);
// 从容器中获取 Bean id+类获取
UserService userService = context.getBean("userService",UserService.class);
// 从容器中获取 Bean id获取
UserService userService =(UserService) context.getBean("userService");
```

# 4. **Bean**

- **定义**：Bean 是由 Spring 容器管理的对象。这些对象通常是应用程序的核心组件。

- **生命周期**：
  
  - 实例化
  
  - 属性赋值
  
  - 初始化（调用 `@PostConstruct` 方法）
  
  - 使用
  
  - 销毁（调用 `@PreDestroy` 方法）

**配置方式**：

- **XML 配置**：通过 `<bean>` 标签定义 Bean。

- **注解配置**：通过 `@Component`、`@Service`、`@Repository`、`@Controller` 等注解定义 Bean。

- **Java 配置**：通过 `@Configuration` 和 `@Bean` 注解定义 Bean。

## 代码

```java
// 注解配置
@Service
public class UserService {
    // ...
}

// Java 配置
@Configuration
public class AppConfig {
    @Bean
    public UserService userService() {
        return new UserServiceImpl();
    }
}
```

# 5. **面向切面编程（AOP, Aspect-Oriented Programming）**

- **定义**：AOP 是一种编程范式，用于将横切关注点（如日志、事务管理、安全性等）从业务逻辑中分离出来。

- **核心概念**：
  
  - **切面（Aspect）**：横切关注点的模块化。
  
  - **连接点（Join Point）**：程序执行过程中的某个点（如方法调用）。
  
  - **通知（Advice）**：在连接点执行的动作（如前置通知、后置通知等）。
  
  - **切入点（Pointcut）**：定义哪些连接点会触发通知。

## 代码

```java
@Aspect
@Component
public class LoggingAspect {
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        System.out.println("Before method: " + joinPoint.getSignature().getName());
    }
}
```

# 6. **Spring MVC**

- **定义**：Spring MVC 是 Spring 框架的一个模块，用于构建基于 MVC 模式的 Web 应用程序。

- **核心组件**：
  
  - **DispatcherServlet**：前端控制器，负责请求的分发。
  
  - **Controller**：处理请求并返回模型和视图。
  
  - **ViewResolver**：解析视图名称并渲染视图。

## 代码

```java
@Controller
public class UserController {
    @GetMapping("/users")
    public String listUsers(Model model) {
        model.addAttribute("users", userService.getAllUsers());
        return "users";
    }
}
```

# 7. **事务管理**

- **定义**：Spring 提供了声明式事务管理，通过注解或 XML 配置管理事务。

- **核心注解**：`@Transactional`。

## ## 代码

```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    @Transactional
    public void createUser(User user) {
        userRepository.save(user);
    }
}
```

# 8. **Spring Boot**

- **定义**：Spring Boot 是 Spring 的扩展，旨在简化 Spring 应用程序的开发和部署。

- **核心特性**：
  
  - 自动配置（Auto-configuration）
  
  - 内嵌服务器（如 Tomcat）
  
  - 简化依赖管理（通过 Starter POMs）

## 代码

```java
@SpringBootApplication
public class MyApp {
    public static void main(String[] args) {
        SpringApplication.run(MyApp.class, args);
    }
}
```

# 9. **Spring Data**

- **定义**：Spring Data 是 Spring 的一个子项目，旨在简化数据访问层的开发。

- **核心模块**：
  
  - Spring Data JPA（用于关系型数据库）
  
  - Spring Data MongoDB（用于 MongoDB）
  
  - Spring Data Redis（用于 Redis）

## 代码

```java
public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByLastName(String lastName);
}
```
