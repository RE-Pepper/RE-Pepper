#pragma once

#include <heap/seadExpHeap.h>
#include <heap/seadFrameHeap.h>
#include <heap/seadHeap.h>
#include <heap/seadHeapMgr.h>

namespace al
{

class MemorySystem
{
private:
        sead::ExpHeap*   mStationedHeap;
        sead::Heap*      _4;
        sead::ExpHeap*   mSequenceHeap;
        sead::FrameHeap* mSceneResourceHeap;
        sead::FrameHeap* mSceneHeap;
        sead::Heap*      _14;
        sead::FrameHeap* mCourseSelectResourceHeap;
        sead::FrameHeap* mCourseSelectHeap;
        u8               unk1[ 0x20 ];

public:
        sead::ExpHeap* getStationedHeap() const
        {
                return mStationedHeap;
        }

        sead::ExpHeap* getSequenceHeap() const
        {
                return mSequenceHeap;
        }

        sead::FrameHeap* getSceneResourceHeap() const
        {
                return mSceneResourceHeap;
        }

        sead::FrameHeap* getSceneHeap() const
        {
                return mSceneHeap;
        }

        sead::FrameHeap* getCourseSelectHeap() const
        {
                return mCourseSelectHeap;
        }

        void createSequenceHeap();
        void createSceneHeap( const char* stageName );
        void createSceneResourceHeap( const char* stageName );

        void destroySceneHeap( bool destroyResource );
        void destroyCourseSelect();

        void freeAllSequenceHeap();
};

void createSequenceHeap();
void createSceneResourceHeap( const char* stageName );
void createSceneHeap( const char* stageName );
void createCourseSelectHeap();

sead::ExpHeap*   getStationedHeap();
sead::ExpHeap*   getSequenceHeap();
sead::FrameHeap* getSceneResourceHeap();
sead::FrameHeap* getSceneHeap();
sead::FrameHeap* getCourseSelectHeap();
sead::FrameHeap* getCourseSelectResourceHeap();

void destroySceneHeap();

bool isCreatedSceneResourceHeap();

class SceneHeapSetter : public sead::ScopedCurrentHeapSetter
{
private:
        sead::Heap* _8;

public:
        SceneHeapSetter();
};

} // namespace al
