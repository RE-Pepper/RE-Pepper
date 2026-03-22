

# File Application.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**System**](dir_aa3fa84a8a04c23ad2697be67b4c7cc2.md) **>** [**Application.cpp**](_application_8cpp.md)

[Go to the documentation of this file](_application_8cpp.md)


```C++
#include "System/Application.h"

#ifdef NON_MATCHING
SEAD_SINGLETON_DISPOSER_IMPL( Application )

Application* al::getApplication()
{
        return Application::instance();
}
#endif
```


