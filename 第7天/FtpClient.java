package com.tlkj;

import org.apache.commons.net.ftp.FTPClient;
import org.apache.commons.net.ftp.FTPFile;
import org.apache.commons.net.ftp.FTPReply;

import java.io.*;

public class FtpClient {
    /**
     * 实现 FTP的文件上传与下载功能
     * 基本知识： 文件流的操作
     *
     * */
    private static boolean uploadFile(
            String url,// FTP服务器hostname
            int port,// FTP服务器端口
            String username, // FTP登录账号
            String password, // FTP登录密码
            String path, // FTP服务器保存目录
            String filename, // 上传到FTP服务器上的文件名
            InputStream input // 输入流
    ) throws IOException {
        boolean success = false;
        FTPClient ftp = new FTPClient();
        ftp.setControlEncoding("GBK");  // windows

        int reply;
        ftp.connect(url, port);// 连接FTP服务器
        // 如果采用默认端口，可以使用ftp.connect(url)的方式直接连接FTP服务器
        ftp.login(username, password);// 登录
        reply = ftp.getReplyCode();
        if (!FTPReply.isPositiveCompletion(reply)) {
            ftp.disconnect();
            return success;
        }
        ftp.setFileType(FTPClient.BINARY_FILE_TYPE);
        ftp.makeDirectory(path);
        ftp.changeWorkingDirectory(path);
        ftp.storeFile(filename, input);
        input.close();
        ftp.logout();
        success = true;

        return success;
    }
    private static void upLoadFromProduction(
            String url,// FTP服务器hostname
            int port,// FTP服务器端口
            String username, // FTP登录账号
            String password, // FTP登录密码
            String path, // FTP服务器保存目录
            String filename, // 上传到FTP服务器上的文件名
            String orginfilename // 输入流文件名
    ){
        FileInputStream in = null;
        try {
            in = new FileInputStream(new File(orginfilename));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        try {
            boolean flag = uploadFile(url, port, username, password, path,filename, in);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * 将FTP服务器上文件下载到本地 *
     */
    public static String downFile(String ftpHost, int port,String username, String password,
                                  String remotePath,String fileName,String localPath) {

        String result = "下载失败 ！";
        FTPClient ftp = new FTPClient();

        try {
            int reply;
            ftp.connect(ftpHost, port);
            ftp.login(username, password); // 登录
            reply = ftp.getReplyCode();
            if (!FTPReply.isPositiveCompletion(reply)) {
                ftp.disconnect();
                return "服务连接失败 ！";
            }

            ftp.changeWorkingDirectory(remotePath); // 转移到FTP服务器目录
            FTPFile[] fs = ftp.listFiles();
            boolean flag = false; // 下载文件不存在
            for(FTPFile ff:fs){
                if(ff.getName().equals(fileName)){
                    File localFile = new File(localPath);
                    OutputStream is = new FileOutputStream(localFile);
                    ftp.retrieveFile(ff.getName(), is);
                    is.close();
                    flag = true;
                }
            }
            ftp.logout();

            if(!flag){
                result = "文件: "+fileName+"不存在 ！";
            }else{
                result = "下载成功 ！";
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (ftp.isConnected()) {
                try {
                    ftp.disconnect();
                } catch (IOException ioe) {}
            }
        }
        return result;
    }




    //测试
    public static void main(String[] args) {
        //上传 端口默认是21， 无用户名则默认： anonymous  ，无密码： "" ， 当前路径path: "./"
        upLoadFromProduction("10.118.61.175", 21, "anonymous", "", "./", "ftsstest.txt", "E:/ftptest.txt");

        //下载
        downFile("10.118.61.175", 21,"anonymous", "", "./","ftptest.txt","D:/ftptest.txt");
    }

}
