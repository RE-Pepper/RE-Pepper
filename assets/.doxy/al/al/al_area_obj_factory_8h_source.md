

# File alAreaObjFactory.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Factory**](dir_3f8e9df3dfd35c77b73e3e3b5744b002.md) **>** [**alAreaObjFactory.h**](al_area_obj_factory_8h.md)

[Go to the documentation of this file](al_area_obj_factory_8h.md)


```C++
#pragma once

#include <AreaObj/alAreaObj.h>
#include <Factory/alFactory.h>

namespace al
{

typedef CreateFuncPtr<AreaObj>::Type        CreateAreaObjFuncPtr;
typedef NameToCreator<CreateAreaObjFuncPtr> NameToAreaObjCreator;

} // namespace al
```


