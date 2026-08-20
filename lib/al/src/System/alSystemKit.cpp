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
