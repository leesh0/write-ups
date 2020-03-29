# RootMe - SpringBoot

> 이번문제는 거의 하루에 걸쳐서 푼 문제이다. 내가 java를 별로 안써보기도 했고 spring boot라는 프레임워크는 처음 접해보기에 구조와 기능을 파악하는게 어려웠다. 역시 웹해킹을 하려면 대략적인 구조는 파악할 수 있도록 한번쯤은 프레임워크를 사용해 보아야 할듯 싶다.

먼저 문제의 힌트로 주어진 것은 `Metrics, a dangerous feature` 이다. Metrics는 Spring Boot에서 제공하는 프로젝트 관리 기능인데 현재 서버의 상태를 보고해주는 역할을 한다.

먼저 해당 챌린지의 metrics를 살펴보자.

[http://challenge01.root-me.org/web-serveur/ch46/metrics](http://challenge01.root-me.org/web-serveur/ch46/metrics)

```javascript
{"mem":420260,"mem.free":295287,"processors":4,"instance.uptime":9726943,"uptime":9736105,"systemload.average":0.3,"heap.committed":365056,"heap.init":192512,"heap.used":69768,"heap":2734592,"nonheap.committed":56704,"nonheap.init":2496,"nonheap.used":55205,"nonheap":0,"threads.peak":14,"threads.daemon":12,"threads.totalStarted":18,"threads":14,"classes":6714,"classes.loaded":6714,"classes.unloaded":0,"gc.ps_scavenge.count":9,"gc.ps_scavenge.time":195,"gc.ps_marksweep.count":2,"gc.ps_marksweep.time":201,"httpsessions.max":-1,"httpsessions.active":0,"gauge.response.root":27.0,"counter.status.200.root":2}
```

이 정만 가지고는 우리가 필요한 정보를 얻을 수 없다. 따라서 다른 actuator의 endpoints들을 확인해보자.

| ID | Description |
| :--- | :--- |
| `auditevents` | Exposes audit events information for the current application. Requires an `AuditEventRepository` bean. |
| `beans` | Displays a complete list of all the Spring beans in your application. |
| `caches` | Exposes available caches. |
| `conditions` | Shows the conditions that were evaluated on configuration and auto-configuration classes and the reasons why they did or did not match. |
| `configprops` | Displays a collated list of all `@ConfigurationProperties`. |
| `env` | Exposes properties from Spring’s `ConfigurableEnvironment`. |
| `flyway` | Shows any Flyway database migrations that have been applied. Requires one or more `Flyway` beans. |
| `health` | Shows application health information. |
| `httptrace` | Displays HTTP trace information \(by default, the last 100 HTTP request-response exchanges\). Requires an `HttpTraceRepository` bean. |
| `info` | Displays arbitrary application info. |
| `integrationgraph` | Shows the Spring Integration graph. Requires a dependency on `spring-integration-core`. |
| `loggers` | Shows and modifies the configuration of loggers in the application. |
| `liquibase` | Shows any Liquibase database migrations that have been applied. Requires one or more `Liquibase` beans. |
| `metrics` | Shows ‘metrics’ information for the current application. |
| `mappings` | Displays a collated list of all `@RequestMapping` paths. |
| `scheduledtasks` | Displays the scheduled tasks in your application. |
| `sessions` | Allows retrieval and deletion of user sessions from a Spring Session-backed session store. Requires a Servlet-based web application using Spring Session. |
| `shutdown` | Lets the application be gracefully shutdown. Disabled by default. |
| `threaddump` | Performs a thread dump. |

여기에 추가적으로 사용될 수 있는 endpoints들은 다음과 같다.

| ID | Description |
| :--- | :--- |
| `heapdump` | Returns an `hprof` heap dump file. |
| `jolokia` | Exposes JMX beans over HTTP \(when Jolokia is on the classpath, not available for WebFlux\). Requires a dependency on `jolokia-core`. |
| `logfile` | Returns the contents of the logfile \(if `logging.file.name` or `logging.file.path` properties have been set\). Supports the use of the HTTP `Range` header to retrieve part of the log file’s content. |
| `prometheus` | Exposes metrics in a format that can be scraped by a Prometheus server. Requires a dependency on `micrometer-registry-prometheus`. |

여기서 나는 사이트의 mapping을 먼저 확인하였다.

**mapping.json**

```javascript
{
   "/webjars/**": {
       "bean": "resourceHandlerMapping"
   },
   "/**": {
       "bean": "resourceHandlerMapping"
   },
   "/**/favicon.ico": {
       "bean": "faviconHandlerMapping"
   },
   "{[/],methods=[GET]}": {
       "bean": "requestMappingHandlerMapping",
       "method": "public java.lang.String org.rootme.metrics.controller.MetricsController.getIndex()"
   },
   "{[/login],methods=[POST]}": {
       "bean": "requestMappingHandlerMapping",
       "method": "public java.lang.String org.rootme.metrics.controller.MetricsController.login(org.rootme.metrics.model.LoginModel)"
   },
   "{[/error],produces=[text/html]}": {
       "bean": "requestMappingHandlerMapping",
       "method": "public org.springframework.web.servlet.ModelAndView org.springframework.boot.autoconfigure.web.BasicErrorController.errorHtml(javax.servlet.http.HttpServletRequest,javax.servlet.http.HttpServletResponse)"
   },
   "{[/error]}": {
       "bean": "requestMappingHandlerMapping",
       "method": "public org.springframework.http.ResponseEntity<java.util.Map<java.lang.String, java.lang.Object>> org.springframework.boot.autoconfigure.web.BasicErrorController.error(javax.servlet.http.HttpServletRequest)"
   },
   "{[/beans || /beans.json],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.EndpointMvcAdapter.invoke()"
   },
   "{[/metrics/{name:.*}],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.MetricsMvcEndpoint.value(java.lang.String)"
   },
   "{[/metrics || /metrics.json],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.EndpointMvcAdapter.invoke()"
   },
   "{[/info || /info.json],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.EndpointMvcAdapter.invoke()"
   },
   "{[/trace || /trace.json],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.EndpointMvcAdapter.invoke()"
   },
   "{[/autoconfig || /autoconfig.json],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.EndpointMvcAdapter.invoke()"
   },
   "{[/heapdump || /heapdump.json],methods=[GET],produces=[application/octet-stream]}": {
       "bean": "endpointHandlerMapping",
       "method": "public void org.springframework.boot.actuate.endpoint.mvc.HeapdumpMvcEndpoint.invoke(boolean,javax.servlet.http.HttpServletRequest,javax.servlet.http.HttpServletResponse) throws java.io.IOException,javax.servlet.ServletException"
   },
   "{[/mappings || /mappings.json],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.EndpointMvcAdapter.invoke()"
   },
   "{[/configprops || /configprops.json],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.EndpointMvcAdapter.invoke()"
   },
   "{[/health || /health.json],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.HealthMvcEndpoint.invoke(java.security.Principal)"
   },
   "{[/env/{name:.*}],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.EnvironmentMvcEndpoint.value(java.lang.String)"
   },
   "{[/env || /env.json],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.EndpointMvcAdapter.invoke()"
   },
   "{[/dump || /dump.json],methods=[GET],produces=[application/json]}": {
       "bean": "endpointHandlerMapping",
       "method": "public java.lang.Object org.springframework.boot.actuate.endpoint.mvc.EndpointMvcAdapter.invoke()"
   }
}
```

mapping의 내용을 보면 `heapdump` 에 익명의 사용자가 접근할 수 있는것을 알 수 있다.

이제 heapdump가 매핑되어 있는 [http://challenge01.root-me.org/web-serveur/ch46/heapdump로가서](http://challenge01.root-me.org/web-serveur/ch46/heapdump로가서) heapdump파일을 다운받는다. heapdump는 \*.hprof확장자를 가지고 있으며 여러 툴에의해 분석가능한데, 대표적으로 IBM사의 MaT가 있다. 하지만 이 프로그램은 다운로드받는데 너무 오래 시간이 걸리므로 따로 java를 설치하면서 함께 제공된 `jhat` 이라는 프로그램을 사용한다.

```text
❯ jhat /Users/leeseungho/Downloads/heapdump2020-01-25-14-09-live9015632950032762638.hprof
Reading from /Users/leeseungho/Downloads/heapdump2020-01-25-14-09-live9015632950032762638.hprof...
Dump file created Sat Jan 25 22:09:51 KST 2020
Snapshot read, resolving...
Resolving 314814 objects...
Chasing references, expect 62 dots..............................................................
Eliminating duplicate references..............................................................
Snapshot resolved.
Started HTTP server on port 7000
Server is ready.
```

이제 [localhost:7000](http://localhost:7000)페이지를 열면 분석된 클래스들이 나열되어 있는것을 확인할 수 있다.

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gb9xv63f7vj31zo0re141.jpg)

아마도 엄청난 수의 클래스들을 보게될텐데 여기서 다른 actuator인 `/beans` 의 json데이터를 확인하며 digging해보다보면

![&#x1109;&#x1173;&#x110F;&#x1173;&#x1105;&#x1175;&#x11AB;&#x1109;&#x1163;&#x11BA; 2020-01-26 15.19.57](https://tva1.sinaimg.cn/large/006tNbRwgy1gb9xx8dfasj30qc042dgi.jpg)

위와 같은 패키지를 확인 할 수가 있는데 이 패키지의 내용을 확인해보면

![&#x1109;&#x1173;&#x110F;&#x1173;&#x1105;&#x1175;&#x11AB;&#x1109;&#x1163;&#x11BA; 2020-01-26 15.20.39](https://tva1.sinaimg.cn/large/006tNbRwgy1gb9xy01zn3j30pg066wfb.jpg)

로그인데이터를 겟할 수 있다.

> 이문제는 노가다성이 꽤 짙은문제여서 나는 여태까지의 문제패턴중에는 노가다가 거의 없었으니까 heapdump는 아니겠지...라는 안일한 생각을 하였는데 큰 오산이었다;

