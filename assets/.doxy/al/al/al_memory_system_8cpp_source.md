

# File alMemorySystem.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Memory**](dir_61087abf9dd1d3f380a1f33ccf7d7be7.md) **>** [**alMemorySystem.cpp**](al_memory_system_8cpp.md)

[Go to the documentation of this file](al_memory_system_8cpp.md)


```C++
#include <Memory/alMemorySystem.h>
#include <Resource/alResource.h>
#include <System/alSystemKit.h>
#include <Util/alStringUtil.h>
#include <Yaml/alByamlIter.h>

namespace al
{

void MemorySystem::createSequenceHeap()
{
        mSequenceHeap = sead::ExpHeap::create( 0, "SequenceHeap", nullptr, sead::ExpHeap::cHeapDirection_Forward, false );
}

extern "C" void fn_002911e8( sead::FrameHeap** out, u32 heapSize, const char* name, u8,
        int ); // creates FrameHeap(?)

#ifdef NON_MATCHING
// WIP
void MemorySystem::createSceneResourceHeap( const char* stageName )
{
        int heapSize;
        if ( stageName )
        {
                al::Resource* gameSystemDataTable =
                        al::findOrCreateResource( "ObjectData/GameSystemDataTable" );
                const u8*     tableData = gameSystemDataTable->getByml( "HeapSizeDefine" );
                al::ByamlIter table( tableData );
                for ( int i = 0; i < table.getSize(); i++ )
                {
                        al::ByamlIter entry;
                        table.tryGetIterByIndex( &entry, i );
                        const char* stage = nullptr;
                        entry.tryGetStringByKey( &stage, "Stage" );
                        if ( al::isEqualString( stage, stageName ) )
                        {
                                float resourceMb = 0;
                                entry.tryGetFloatByKey( &resourceMb, "SceneResource" );
                                heapSize = resourceMb * 1024 * 1024;
                                break;
                        }
                }
        }
        else
                heapSize = 8 * 1024 * 1024; // 8 MB
        fn_002911e8( &mSceneResourceHeap, heapSize, "SceneHeapResource", 0, 1 );
}
#endif

void MemorySystem::freeAllSequenceHeap()
{
        mSequenceHeap->freeAll();
}

sead::ExpHeap* getStationedHeap()
{
        return alProjectInterface::getSystemKit()->getMemorySystem()->getStationedHeap();
}

sead::ExpHeap* getSequenceHeap()
{
        return alProjectInterface::getSystemKit()->getMemorySystem()->getSequenceHeap();
}

sead::FrameHeap* getSceneResourceHeap()
{
        return alProjectInterface::getSystemKit()->getMemorySystem()->getSceneResourceHeap();
}

sead::FrameHeap* getCourseSelectHeap()
{
        return alProjectInterface::getSystemKit()->getMemorySystem()->getCourseSelectHeap();
}

bool isCreatedSceneResourceHeap()
{
        return getSceneResourceHeap() != nullptr;
}

} // namespace al
```


