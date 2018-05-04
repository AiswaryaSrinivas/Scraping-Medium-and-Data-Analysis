# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:51:19 2018

@author: Aiswarya

Extract Data from json files created using medium_scrapper_tag_archive.py

"""

#from scrapperFunctions import *
import pandas as pd
import datetime
import codecs
import os
import json
#import sqlalchemy
#import urllib
os.chdir("D:\Aiswarya\Web Scraping\medium_scrapper\\")

def writeTofile(fileName,text):
    with codecs.open(fileName,'w','utf-8') as outfile:
        outfile.write(text)


def getJsonResponse(fileName):
    with codecs.open(fileName,'r','utf-8') as infile:
        data=json.load(infile)
    return data

#Check if success True in json
def isRequestSuccess(data):
    if "success" in data:
        #print "success in data" 
        #print data["success"]
        if data["success"]==True:
            return True
    return False

def hasPayload(data):
    if "payload" in data:
        return True
    else:
        return False

def hasTopicTag(data):
    if hasPayload(data)==True:
        data=data["payload"]
        if "topic" in data:
            return True
    return False

def hasReferenceTag(data):
    if hasPayload(data)==True:
        data=data["payload"]
        if "references" in data:
            return True
    return False

def processPost(dat):
    print("In Process Post")
    posts_dict={}
    tags=pd.DataFrame()
    posts=pd.DataFrame()
    posts_dict["id"]=[dat["id"]]
    print(dat["id"])
    posts_dict["versionId"]=[dat["versionId"]]
    print(dat["creatorId"])
    posts_dict["creatorId"]=[dat["creatorId"]]
    posts_dict["collectionId"]=[dat["homeCollectionId"]]
    
    posts_dict["title"]=[dat["title"]]
    posts_dict["language"]=[dat["detectedLanguage"]]
    posts_dict["createdAt"]=[dat["createdAt"]]
    posts_dict["updatedAt"]=[dat["updatedAt"]]
    posts_dict["firstPublishedAt"]=[dat["firstPublishedAt"]]
    posts_dict["latestPublishedAt"]=[dat["latestPublishedAt"]]
    posts_dict["story_slug"]=[dat["slug"]]
    posts_dict["uniqueSlug"]=[dat['uniqueSlug']]
    posts_dict["vote"]=[dat['vote']]
    posts_dict["hasUnpublishedEdits"]=[dat["hasUnpublishedEdits"]]
    posts_dict["allowResponses"]=[dat["allowResponses"]]
    posts_dict["importedUrl"]=[dat["importedUrl"]]
    posts_dict["webCanonicalUrl"]=[dat["webCanonicalUrl"]]
    posts_dict["mediumUrl"]=[dat["mediumUrl"]]
    posts_dict["importedPublishedAt"]=[dat["importedPublishedAt"]]
    posts_dict["vote"]=[dat["vote"]]
    posts_dict["isApprovedTranslation"]=[dat["isApprovedTranslation"]]
    posts_dict["translationSourcePostId"]=[dat["translationSourcePostId"]]
    posts_dict["translationSourceCreatorId"]=[dat["translationSourceCreatorId"]]
    posts_dict["displayAuthor"]=[dat["displayAuthor"]]
    posts_dict["coverless"]=[dat["coverless"]]
    #What type of preview content are available 
    prev_name=[]
    prev_type=[]
    prev_text=[]
            
    for prev_content in dat["previewContent"]["bodyModel"]["paragraphs"]:
        #print prev_content['name']
        if "name" in prev_content:
            prev_name.append(prev_content["name"])
        else:
            prev_name.append("")
        if "type" in prev_content:
            prev_type.append(prev_content["type"])
        else:
            prev_type.append("")
                
        if("text" in prev_content):
            #print "Text tag present"
            text=prev_content["text"]
                    
            prev_text.append(text)
            #print "Priting prev Text list"
            #print prev_text
        else:
            prev_text.append("")
    posts_dict["PreviewContent_Name"]=[prev_name]
    posts_dict["PreviewContent_Type"]=[prev_type]
    posts_dict["PreviewContent_Text"]=[prev_text]
    posts_dict["PreviewContent_isFullContent"]=[dat["previewContent"]["isFullContent"]]
    posts_dict["notifyFollowers"]=[dat["notifyFollowers"]]
    posts_dict["notifyTwitter"]=[dat["notifyTwitter"]]
    posts_dict["notifyFacebook"]=[dat["notifyFacebook"]]
    posts_dict["isSeries"]=[dat["isSeries"]]
    posts_dict["isSponsored"]=[dat["isSponsored"]]
    posts_dict["isSubscriptionLocked"]=[dat["isSubscriptionLocked"]]
    posts_dict["seriesLastAppendedAt"]=[dat["seriesLastAppendedAt"]]
    posts_dict["audioVersionDurationSec"]=[dat["audioVersionDurationSec"]]
    posts_dict["isNsfw"]=[dat["isNsfw"]]
    posts_dict["isEligibleForRevenue"]=[dat["isEligibleForRevenue"]]
    posts_dict["isBlockedFromHightower"]=[dat["isBlockedFromHightower"]]
    posts_dict["featureLockRequestAcceptedAt"]=[dat["featureLockRequestAcceptedAt"]]
    posts_dict["featureLockRequestMinimumGuaranteeAmount"]=[dat["featureLockRequestMinimumGuaranteeAmount"]]
    posts_dict["isElevate"]=[dat['isElevate']]
    posts_dict["isTitleSynthesized"]=[dat["isTitleSynthesized"]]
    posts_dict["inResponseToPostId"]=[dat["inResponseToPostId"]]
            
            
            #Get metadata from virtuals
    if "virtuals" in dat:
        virtuals=dat["virtuals"]
        #print virtuals
        if "statusForCollection" in virtuals:
            posts_dict["statusForCollection"]=[virtuals["statusForCollection"]]
        else:
            posts_dict["statusForCollection"]=[""]
                    
        posts_dict["allowNotes"]=[virtuals["allowNotes"]]
        posts_dict["wordCount"]=[virtuals["wordCount"]]
        posts_dict["imageCount"]=[virtuals["imageCount"]]
        posts_dict["readingTime"]=[virtuals["readingTime"]]
        posts_dict["subTitle"]=[virtuals["subtitle"]]
        if "publishedInCount" in virtuals:
            posts_dict["publishedInCount"]=[virtuals["publishedInCount"]]
        else:
            posts_dict["publishedInCount"]=[""]
        posts_dict["recommends"]=[virtuals["recommends"]]
        posts_dict["isBookmarked"]=[virtuals["isBookmarked"]]
        posts_dict["socialRecommendsCount"]=[virtuals["socialRecommendsCount"]]
        posts_dict["responsesCreatedCount"]=[virtuals["responsesCreatedCount"]]
        posts_dict["isLockedPreviewOnly"]=[virtuals["isLockedPreviewOnly"]]
        posts_dict["sectionCount"]=[virtuals["sectionCount"]]
        posts_dict["metaDescription"]=[virtuals["metaDescription"]]
        posts_dict["totalClapCount"]=[virtuals["totalClapCount"]]
        posts_dict["readingList"]=[virtuals["readingList"]]
                
        #Get number of links in the story
        try:
            posts_dict["linksCount"]=len(virtuals["links"]["entries"])
        except:
            posts_dict["linksCount"]=0
                #Get number of tags in the story
        posts_dict["tagsCount"]=len(virtuals["tags"])
                #What are the tags associated with the story
        tag_name=[]
        tag_slug=[]
        tags_dict={}
        for tag in virtuals["tags"]:
            tag_slug.append(tag["slug"])
            tag_name.append(tag["name"])
            tags_dict["slug"]=[tag["slug"]]
            tags_dict["name"]=[tag["name"]]
            tags_dict["followerCount"]=[tag['metadata']["followerCount"]]
            tags_dict["postCount"]=[tag['metadata']["postCount"]]
            tags_dict["isFollowing"]=[tag['virtuals']['isFollowing']]
                    
        tags=tags.append(pd.DataFrame(tags_dict),ignore_index=False)
        posts_dict["tags_slug"]=[tag_slug]
        posts_dict["tags_name"]=[tag_name]
    posts=posts.append(pd.DataFrame(posts_dict),ignore_index=True)
    return [posts,tags]
 

def ReadData(path):
    posts=pd.DataFrame()
    tags=pd.DataFrame()
    users=pd.DataFrame()
    collections=pd.DataFrame()
    files=os.listdir(path)
    
    #files=["dataScienceTag20180430.json"]
    processedFiles=[]
    
    #total_records_processed=0
    
    for fileName in files :
        if '.json' in fileName:
            with codecs.open(path+fileName,'r','utf-8') as infile:
                data=json.load(infile)
            
            dfs=processTopicPost(data)
            posts=posts.append(dfs[0],ignore_index=True)
            tags=tags.append(dfs[1],ignore_index=True)
            posts['searchTag']=fileName.split("Tag")[0]
            print(fileName.split("Tag")[0])
            archiveDate=fileName.split("Tag")[1]
            archiveDate=archiveDate.strip(".json")
            archiveDate=datetime.datetime.strptime(archiveDate, '%Y%m%d').strftime("%Y-%m-%d")
            posts['archiveDate']=archiveDate
            scrappedDate=path.strip("\\")
            posts['scrappedDate']=datetime.datetime.strptime(scrappedDate, '%Y%m%d').strftime("%Y-%m-%d")
            tags['scrappedDate']=datetime.datetime.strptime(scrappedDate, '%Y%m%d').strftime("%Y-%m-%d")
            references=processReferences(data,fileName.split("Tag")[1],scrappedDate)
            users=users.append(references[0],ignore_index=True)
            collections=collections.append(references[1],ignore_index=True)               
            processedFiles.append(fileName)
    
    posts.to_csv(path+"Posts_ByTag_"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".csv",index=False,encoding='utf-8')
    tags.to_csv(path+"Tags_ByTag_"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".csv",index=False,encoding='utf-8')
    users.to_csv(path+"Users_ByTag_"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".csv",index=False,encoding='utf-8')
    collections.to_csv(path+"Collections_ByTag_"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".csv",index=False,encoding='utf-8')    
    
def processTopicPost(data):
    
    #Check if request successful
    successStatus=isRequestSuccess(data)
    print(successStatus)
    postdata=pd.DataFrame()
    tags=pd.DataFrame()
    #check if references in payload
    if successStatus==True and hasReferenceTag(data)==True:
        data=data["payload"]["references"]
        if "Post" in data:
            posts=data["Post"]
            #Get all the post id
            post_id=[]
            for post in posts:
                post_id.append(post)
            #For each post id extract post information
            for pid in post_id:
                #print(pid)
                post=posts[pid]
                dfs=processPost(post)
                postdata=postdata.append(dfs[0],ignore_index=True)
                tags=tags.append(dfs[1],ignore_index=True)
    #postdata.to_csv("Posts.csv",encoding='utf-8')
    #tags.to_csv("Tags.csv",encoding='utf-8')
    return [postdata,tags]




    #If success, check if payload exists
def processReferences(data_json,searchTag,dateScrapped):
    user_df=pd.DataFrame()
    collection_df=pd.DataFrame()
    flag=False
    
    if "success" in data_json:
        if "payload" in data_json:
            if "references" in data_json["payload"]:
                print("references present")
                #print data_json["payload"]["value"]
                flag=True
    if flag==True:
        data=data_json["payload"]["references"]
        if "User" in data:
            user_dict={}
            users=data["User"]
            #print len(users)
            #print type(users)
            user_key=[]
            for user in users:
                user_key.append(user)
            for key in user_key:
                user=users[key]
                user_dict["Search Tag"]=[searchTag]
                user_dict["ScrappedDate"]=[ datetime.datetime.strptime(dateScrapped, '%Y%m%d').strftime("%Y-%m-%d")]
                user_dict["userId"]=[user["userId"]]
                user_dict["Name"]=[user["name"]]
                user_dict["userName"]=[user["username"]]
                user_dict["createdAt"]=[user["createdAt"]]
                user_dict["lastPostCreatedAt"]=[user["lastPostCreatedAt"]]
                user_dict["bio"]=[user["bio"]]
                if "twitterScreenName" in user:
                    user_dict["twitterScreenName"]=[user["twitterScreenName"]]
                else:
                    user_dict["twitterScreenName"]=[""]
                if "facebookAccountId" in user:
                    user_dict["facebookAccountId"]=[user["facebookAccountId"]]
                else:
                    user_dict["facebookAccountId"]=[""]
                user_dict["allowNotes"]=[user["allowNotes"]]
                user_dict["mediumMemberAt"]=[user["mediumMemberAt"]]
                if "isNsfw" in user:
                    user_dict["isNsfw"]=[user["isNsfw"]]
                else:
                    user_dict["IsNsfw"]=[""]
                user_df=user_df.append(pd.DataFrame(user_dict),ignore_index=True)
        if "Collection" in data:
            collection_dict={}
            collections=data["Collection"]
            collection_key=[]
            for collection in collections:
                collection_key.append(collection)
            for key in collection_key:
                coll=collections[key]
                collection_dict["Search Tag"]=[searchTag]
                collection_dict["ScrappedDate"]=[ datetime.datetime.strptime(dateScrapped, '%Y%m%d').strftime("%Y-%m-%d")]
                collection_dict['id']=[coll["id"]]
                collection_dict["name"]=[coll["name"]]
                collection_dict["slug"]=[coll["slug"]]
                if "tags" in coll:
                    collection_dict["tags"]=[coll["tags"]]
                else:
                    collection_dict["tags"]=""
                collection_dict["creatorId"]=[coll["creatorId"]]
                collection_dict["description"]=[coll["description"]]
                collection_dict["shortDescription"]=[coll["shortDescription"]]
                collection_dict["followerCount"]=[coll["metadata"]["followerCount"]]
                if "twitterUsername" in coll:
                    collection_dict["twitterUsername"]=[coll["twitterUsername"]]
                else:
                    collection_dict["twitterUsername"]=[""]
                if "facebookPageName" in coll:
                    collection_dict["facebookPageName"]=[coll["facebookPageName"]]
                else:
                    collection_dict["facebookPageName"]=[""]
                if "publicEmail" in coll:
                    collection_dict["publicEmail"]=[coll["publicEmail"]]
                else:
                    collection_dict["publicEmail"]=[""]
                if "domain" in coll:
                    
                    collection_dict["domain"]=[coll["domain"]]
                else:
                    collection_dict["domain"]=[""]
                if "lightText" in coll:
                    collection_dict["lightText"]=[coll["lightText"]]
                else:
                    collection_dict["lightText"]=[""]
                if "instantArticlesState" in coll:
                    
                    collection_dict["instantArticlesState"]=[coll["instantArticlesState"]]
                else:
                    collection_dict["instantArticlesState"]=[""]
                if "acceleratedMobilePagesState" in coll:
                    collection_dict["acceleratedMobilePagesState"]=[coll["acceleratedMobilePagesState"]]
                else:
                    collection_dict["acceleratedMobilePagesState"]=[""]
                collection_df=collection_df.append(pd.DataFrame(collection_dict),ignore_index=True)
                
                
                    
                        
                
            
        
        return [user_df,collection_df]
                
                
                



# Read Data by giving folder path

ReadData("20180504\\")
