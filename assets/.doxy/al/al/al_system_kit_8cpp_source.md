

# File alSystemKit.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**System**](dir_e49b8d878483a20348427946fadd634d.md) **>** [**alSystemKit.cpp**](al_system_kit_8cpp.md)

[Go to the documentation of this file](al_system_kit_8cpp.md)


```C++
#include <File/alFileLoader.h>
#include <Save/alSaveDataDirector.h>
#include <System/Application.h>
#include <System/alSystemKit.h>

namespace al
{

void SystemKit::createFileLoader( int r1 )
{
        mFileLoader = new FileLoader( r1 );
}

void SystemKit::createSaveDataSystem( u32 r1, s32 r2 )
{
        mSaveDataDirector = new SaveDataDirector( r1, r2 );
}

} // namespace al

namespace alProjectInterface
{

al::SystemKit* getSystemKit()
{
        return al::getApplication()->getSystemKit();
}

} // namespace alProjectInterface
```


