

# File alAreaObjFactory.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Factory**](dir_5efa9ffebf04d5a5d0ccd42b7f05d549.md) **>** [**alAreaObjFactory.h**](al_area_obj_factory_8h.md)

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


